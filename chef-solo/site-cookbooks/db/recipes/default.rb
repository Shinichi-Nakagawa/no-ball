#
# Cookbook Name:: wbm_database
# Recipe:: default
#
# Copyright 2014, YOUR_COMPANY_NAME
#
# All rights reserved - Do Not Redistribute
#

include_recipe 'mysql::server'

mysql_service 'default' do
  remove_test_database true
  server_root_password 'root password'
  action :create
end
