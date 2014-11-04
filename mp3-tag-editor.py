#MP3 Tag Editor By Pradd.
#Version 1.0 Apache 2.0 License. Copyright 2014
import eyed3,urllib2,re,json,os,sys

def getFiles(params):
      inputlist= os.listdir(params)
      outputlist=[]
      for data in inputlist:
            outputlist.append(params+data)
      return outputlist

def getAlbumArt(function,artist,name):
      try:
            
            url="http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key=348b4a08fda8a9b3c5a1ab7b2937f071&artist={0}&track={1}&format=json".format(artist.lower(),name.lower())
            url=url.replace(' ','%20')
            
      
            urldata=urllib2.urlopen(url)
            data=urldata.read()
      
      
            js=json.loads(data)
            
            imagelink=js['track']['album']['image'][2]['#text']
            return imagelink
      except:
            
            return False
def loadfile(location):
      audiofile=eyed3.load(location)
      print "Opened {0} in EyeD3".format(location)
      return audiofile
def getData(name):
      url='http://tinysong.com/b/{0}?format=json&key=ac948d3bb6b0c253274f5e4d52bf9543'.format(name) #You can use your own API key as well
      urldata=urllib2.urlopen(url)
      data=urldata.read()
      

      if len(data)<10:
            print "No JSON data available for {0}. Skipping it.\n".format(name)
            return False
      else:
            jsondata=json.loads(data)
            return jsondata

def modify(function, jsondata,name,artist=True,album=True,albumartist=False):
      
      artist=jsondata['ArtistName']
      album=jsondata['AlbumName']
      print "Modifying tag data of {0} \n".format(name)
      
      function.tag.artist=artist
      function.tag.album=album
      name=name.replace(artist,'')
      name=name.replace('-','')
      print name
      picture=getAlbumArt(function,artist,name)
      if picture:
            print "Album Art found"
            imagedata = urllib2.urlopen(picture).read()
            function.tag.images.set(3,imagedata,"image/jpeg",u"you can put a description here")
      else:
            print "Album Art Not Found.."
      
      function.tag.save()
      return True,artist


def main():
      
      for file in getFiles(folder):
            try:
                  function=loadfile(file)
                  jsondata=getData(function.tag.title)
                  
                  if not jsondata:
                        pass
                  else:
                  
                        status, art=modify(function,jsondata,function.tag.title)
            except:
                  pass
            
                 

      print "Thanks for using..."

if __name__=='__main__':
      if len(sys.argv)==1:
            folder="C:/music/" #Enter Folder name here
      else:
            folder=sys.argv[1]
            
      print "Welcome to MP3 Tag Editor Python Script By Pradd. \n\n"
      main()



