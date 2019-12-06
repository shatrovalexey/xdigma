from math import ceil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import argparse
import re
import traceback

argv = argparse.ArgumentParser( description = 'Веб-краулер' )
argv.add_argument( '--galaxy' , type = int , help = '№ галактики' )
argv.add_argument( '--galaxy_from' , type = int , help = '№ галактики от' )
argv.add_argument( '--galaxy_to' , type = int , help = '№ галактики до' )
argv.add_argument( '--system_from' , type = int , help = '№ систем от' )
argv.add_argument( '--system_to' , type = int , help = '№ систем до' )
argv.add_argument( '--login' , required = True , help = 'Логин' )
argv.add_argument( '--password' , required = True , help = 'Пароль' )
argv.add_argument( '--grab' , help = 'Автосбор' )
args = argv.parse_args( )

if 'galaxy' not in args or args.galaxy is None :
	if args.galaxy_from is None : args.galaxy_from = 1
	if args.galaxy_to is None : args.galaxy_to = 8

	galaxyes = range( args.galaxy_from , args.galaxy_to + 1 )
else :
	galaxyes = [ args.galaxy ]

if 'system' not in args or args.system is None :
	if args.system_from is None : args.system_from = 180
	if args.system_to is None : args.system_to = 230

	systems = range( args.system_from , args.system_to + 1 )
else :
	systems = [ args.system ]

planets = range( 1 , 14 )

options = Options( )
options.add_experimental_option( 'prefs' , {
	'profile.managed_default_content_settings.images' : 2 ,
	'plugins.plugins_disabled' : [ 'Shockwave Flash' ]
} )
for option in [
	'disable-infobars' , 'start-maximized' ,
	'--no-sandbox' , '--disable-dev-shm-usage' , '--headless' , '--disable-gpu' , '--disable-extensions' ,
	'User-Agent=Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'
] : options.add_argument( option )

url_match = re.compile( '.*?\?page=fleetTable&galaxy=\d+&system=\d+&planet=(\d+)&planettype=(\d+)&target_mission=(\d+)\'>(.+)' )

try :
	wdh = webdriver.Chrome( executable_path = '/usr/lib/chromium-browser/chromedriver' , chrome_options = options )
	wdh.get( 'https://xdigma.ru/uni03/index.php' )

	form = wdh.find_element_by_id( 'login' )
	field = form.find_element_by_name( 'username' )
	field.send_keys( args.login )

	field = form.find_element_by_name( 'password' )
	field.send_keys( args.password )
	field.send_keys( Keys.RETURN )

	for galaxy in galaxyes :
		print( '%s:xxx:xxx' % galaxy )
		for system in systems :
			print( '%s:%s:xxx' % ( galaxy , system ) )
			wdh.get( 'https://xdigma.ru/uni03/game.php?page=galaxy2d&galaxy=%s&system=%s' % ( galaxy , system ) )

			for content in [
				a_node.get_attribute( 'data-tooltip-content' )
				for a_node in wdh.find_elements_by_xpath( '//a[@class="tooltip_sticky"][@data-tooltip-content]' )
			] :
				for content_item in content.split( ) :
					matches = url_match.match( content_item )

					if not matches : continue

					( planet , planet_type , target_mission , title ) = matches.group( 1 , 2 , 3 , 4 )

					if target_mission in [ '1' , '3' , '4' , '5'  '9' , '16' ] : continue

					content_item = re.sub( r'<.*?>' , ' ' , content )
					content_item = re.sub( r'\s+' , ' ' , content_item )

					if target_mission not in [ '12' , '19' ] : continue

					if args.grab is None :
						if target_mission in [ '12' , '19' ] :
							print( content_item )
						else :
							print( '%s: %s:%s:%s' % ( title , galaxy , system , planet ) )

						continue

					print( content_item )
					print( target_mission )

					wdh.get( 'https://xdigma.ru/uni03/game.php?page=fleetTable' )

					try :
						field = wdh.find_element_by_name( 'ship209' )
					except :
						print( 'Ships not found' )
						continue

					try :
						if target_mission == '8' :
							ships_count = 200
						elif target_mission == '12' :
							ships_count = 200
						else :
							ships_count = 10

						field.clear( )
						field.send_keys( ships_count )
						field.send_keys( Keys.RETURN )

						field = wdh.find_element_by_xpath( '//*[@id="galaxy"]' )
						field.clear( )
						field.send_keys( galaxy )

						field = wdh.find_element_by_xpath( '//*[@id="system"]' )
						field.clear( )
						field.send_keys( system )

						field = wdh.find_element_by_xpath( '//*[@id="planet"]' )
						field.clear( )
						field.send_keys( planet )

						wdh.execute_script( 'document.forms["form"].submit( )' )

						field = wdh.find_element_by_xpath( '//*[@id="radio_%s"]' % target_mission )
						field.click( )
						field.send_keys( Keys.RETURN )

						print( 'sent %s' % ships_count )
					except Exception as exception :
						print( exception )
except Exception as exception :
	print( exception )
	print( traceback.format_exc( ) )
finally : wdh.quit( )
