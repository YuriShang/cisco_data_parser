CODE =  .

build:
	docker-compose -f docker-compose.yml up cisco_parser

show_all:
	docker-compose run cisco_parser 0 

show_version:
	docker-compose run cisco_parser 1
	
show_startup:
	docker-compose run cisco_parser 2
	
show_running:
	docker-compose run cisco_parser 3
	
show_acl:
	docker-compose run cisco_parser 4

show_interface:
	docker-compose run cisco_parser 5

	
