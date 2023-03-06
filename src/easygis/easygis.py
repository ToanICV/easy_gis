import json
import os
import sys

class egis:
    def __init__(self,country):
        self.country = country
        
    def loadDatabase(self):
        print(f"[DEBUG] {os.getcwd()}")
        f = open(os.path.join(sys.prefix + '\\gis_data\\' + self.country + '.json'),encoding='utf8')
        return json.load(f)
    
    def pointInPolygon(self,pts,poly):
        i = 0
        j=len(poly)-1
        oddNodes = False
        for i in range(0,len(poly)):
            if (((poly[i][0]< pts[1]) and (poly[j][0]>=pts[1]) or (poly[j][0]< pts[1]) and (poly[i][0]>=pts[1])) and ((poly[i][1]<=pts[0]) or (poly[j][1]<=pts[0]))):
                oddNodes^=(poly[i][1]+(pts[1]-poly[i][0])/(poly[j][0]-poly[i][0])*(poly[j][1]-poly[i][1])<pts[0]) 
            j=i
        return oddNodes
    
    def findout(self,pts,db):
        nWard = len(db)
        for idxDtr in range(0,nWard):
            ret = self.pointInPolygon(pts,db[idxDtr]["coordinates"])
            if (ret == True):
                return {
                    "ward" : db[idxDtr]["ward"],
                    "district" : db[idxDtr]["district"],
                    "province" : db[idxDtr]["province"]
                }
            if ((ret == False) and (idxDtr == nWard -1 )):
                return {
                    "ward" : None,
                    "district" : None,
                    "province" : None
                }