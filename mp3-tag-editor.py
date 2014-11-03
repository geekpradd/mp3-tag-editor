import eyed3,urllib2,json,os,sys

def getFiles(params):
      inputlist= os.listdir(params)
      outputlist=[]
      for data in inputlist:
            outputlist.append(params+data)
      return outputlist

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

      function.tag.save()
      return True

def main():
      
      for file in getFiles(folder):
            try:
                  function=loadfile(file)
                  jsondata=getData(function.tag.title)
                  if not jsondata:
                        pass
                  else:
                  
                        modify(function,jsondata,function.tag.title)
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



