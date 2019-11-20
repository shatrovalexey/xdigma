import re

str = """
<table style='width:220px'><tr><th colspan='2'>Астероид [3:204:13] <br>Мет:4,7&nbsp;M / Крис:774&nbsp;K / Дейт:0&nbsp;</th></tr><tr><td style='width:80px'><img src='./styles/theme/gow/planeten/small/2d/s_asteroid.png' height='75' width='75' alt=></td><td>
																		<a href='?page=fleetTable&galaxy=3&system=204&planet=13&planettype=1&target_mission=12'>Сбор Астероида</a><br>			
						
						
												
			
						
			</td></tr></table>
"""

url_match = re.compile( '.*?\?page=fleetTable&galaxy=\d+&system=\d+&planet=(\d+)&planettype=(\d+)&target_mission=(\d+)\'>(.+)' )


for s in str.split( ) :
	r = url_match.match( s )

	if not r : continue

	print( r.group( 4 ) )