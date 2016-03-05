# python 3
# This is demo file. Don't run it

from ftplib import FTP

ftp=FTP('domain.com')
ftp.login(user='user',passwd='password')

#ftp.cwd('/sub-donain-name/')

def grabFile():
    filename='graphdata.csv'
    localfile=open(filename,'wb')
    ftp.retrbinary('RETR ' + filename , localfile.write , 1024)
    ftp.quit()
    localfile.close()

def placeFile():
    filename='graphdata.csv'
    ftp.storebinary('STOR ' + filename , open(filename , 'rb'))
    ftp.quit()
