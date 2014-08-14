#
# Cookbook Name:: migrate
# Recipe:: default
#
# Copyright 2014, YOUR_COMPANY_NAME
#
# All rights reserved - Do Not Redistribute
#
include_recipe 'database::mysql'

mysql_connection_info = {:host => "localhost",
                         :username => 'root',
                         :password => node['mysql']['server_root_password']}


# create database
mysql_database node['database']['name'] do
  connection mysql_connection_info
  action :create
end

# create & grant admin username
mysql_database_user node['database']['user']['admin']['name'] do
  connection mysql_connection_info
  password node['database']['user']['admin']['password']
  database_name node['database']['name']
  privileges [:all]
  action [:create, :grant]
end


# create & grant application user
mysql_database_user node['database']['user']['app']['name'] do
  connection mysql_connection_info
  password node['database']['user']['app']['password']
  database_name node['database']['name']
  privileges [:select, :update, :insert, :delete]
  action [:create, :grant]
end