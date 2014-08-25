
# Create your views here.


from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from django.views.generic import TemplateView
from noball_django.settings import VIEW_ENCODE
from service.const import MAX_YEAR, LEAGUE_AL, LEAGUES
from mlb.form import SearchForm, PytagorasForm
from mlb.service.mlb_service import MLBService
from mlb.models import Team


class BaseView(TemplateView):

    def get_context_data(self, **kwargs):
        # Serviceのインスタンス
        self.service = MLBService(VIEW_ENCODE)
        # 共通処理（野手・投手共通の処理、DB検索など）
        context = super(TemplateView, self).get_context_data(**kwargs)
        # 固定値を取得
        context.update(self.service.get_base_context())
        return context


class TopView(BaseView):
    template_name = "%s/top.html" % (MLBService.SUB_DOMAIN)

    def get_context_data(self, **kwargs):
        context = super(TopView, self).get_context_data(**kwargs)
        # TODO 多分何も出さない
        return context


class HomeView(BaseView):
    template_name = "%s/home.html" % (MLBService.SUB_DOMAIN)

    def get_context_data(self, **kwargs):
        context = super(TopView, self).get_context_data(**kwargs)
        # TODO ここに、プロフィールを出す実装
        return context


class PythagorasView(BaseView):
    template_name = "%s/pythagoras.html" % (MLBService.SUB_DOMAIN)

    def get_context_data(self, **kwargs):
        context = super(PythagorasView, self).get_context_data(**kwargs)
        context['year'], context['league'], context['leagues'] = MAX_YEAR, LEAGUE_AL, LEAGUES
        teams = Team.objects.filter(yearID=context['year']).filter(lgID=context['league']).order_by('divID', 'Rank')
        context['dataset'] = self.service.get_pythagoras_dataset(teams)
        return context



def _search(request, action):
    service = MLBService(VIEW_ENCODE)
    form = SearchForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data[MLBService.QUERY_KEY]
        # 件数チェック
        players = Team.objects.filter(search_name=name.lower())
        if players.count() == 1:
            # リダイレクト先設定
            url = '/%s/%s/?%s=%s' % (MLBService.SUB_DOMAIN, action, MLBService.QUERY_KEY, name)
            return HttpResponseRedirect(url)

        # 0件又は複数件
        context = service.get_base_context()
        context['MENU_ENABLE'] = False
        context['query_name'] = name
        context['count'] = players.count()
        context['values'] = []
        context['title'] = ''
        context['action'] = action
        if action == 'home':
            context['search_action'] = 'search'
        else:
            context['search_action'] = '%s_search' % action


        template_html = '%s/%s.html' % (MLBService.SUB_DOMAIN, 'search_result')
        # TODO カウント毎に画面を分ける
        if players.count() > 1:
            # 候補選手を出してあげる
            for player in players:
                context['values'].append(player)
        else:
            # 0件なら結果なし
            # 1件以上なら「もしかして？XX」を出す（3,4件?）
            like_players = Team.objects.filter(search_name__contains=name.lower())
            for like_player in like_players:
                context['values'].append(like_player)

        if len(context['values']):
            context['result'] = True
        else:
            context['result'] = False

        return render_to_response(
            template_html, context, context_instance=RequestContext(request)
        )
    else:
        # validateエラー
        # リダイレクト先設定
        template_html = '%s/%s.html' % (MLBService.SUB_DOMAIN, action)
        context = service.get_base_context()
        # 検索QUERYを保存
        context['query_name'] = ''
        context['error_message'] = u"検索ワード不正。"
        return render_to_response(
            template_html, context, context_instance=RequestContext(request)
        )


def search(request):
    if request.method == 'POST':
        return _search(request, 'home')


def pythagoras_search(request):
    """
    ピタゴラス勝率(Form検索)
    :param request: request object
    :return: html
    """
    service = MLBService(VIEW_ENCODE)
    context = service.get_base_context()
    template_html = "%s/pythagoras.html" % (MLBService.SUB_DOMAIN)

    if request.method == 'POST':
        form = PytagorasForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            league = form.cleaned_data['league']
            context['year'], context['league'], context['leagues'] = year, league, LEAGUES
            teams = Team.objects.filter(yearID=context['year']).filter(lgID=context['league']).order_by('divID', 'Rank')
            context['dataset'] = service.get_pythagoras_dataset(teams)
            context['search_action'] = 'pythagoras_search'
        return render_to_response(
            template_html, context, context_instance=RequestContext(request)
        )



