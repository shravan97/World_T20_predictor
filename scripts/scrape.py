from bs4 import BeautifulSoup
import urllib2

team_no = raw_input('Enter the team number as in cricinfo : ')
stop_date = raw_input('Enter the stop date : ')

content = urllib2.urlopen('http://stats.espncricinfo.com/ci/engine/team/'+team_no+'.html?class=2;host=4;spanmin1=01+Jan+2000;spanval1=span;template=results;type=team;view=results').read()
c = BeautifulSoup(content)
k = c.find_all('table')
k1 = k[len(k)-4]
k_rows = k1.find_all('tr')
tot=0
w=0
for m in range(1,35):
    kr = k_rows[m]
    kcols_res = kr.find_all('td' , {'class':'left'})
    kcols_date = kr.find_all('td' , {'nowrap':'nowrap'})
    kcols_res1 = kcols_res[0]
    kb = kr.find_all('b')
    if kcols_res1.decode_contents(formatter='html') != 'lost':
        w+=1
    tot+=1
    if kb[0].decode_contents(formatter='html') == stop_date:
        break
print w , ',' , tot