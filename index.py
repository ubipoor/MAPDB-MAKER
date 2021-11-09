import os, json, matplotlib

with open("songdesc.tpl.ckd") as songdesctpl:
    songdesc=json.load(songdesctpl)

codename=songdesc["COMPONENTS"][0]["MapName"]
codenamelow=codename.lower()

with open(codenamelow+"_musictrack.tpl.ckd") as mttpl:
    mt=json.load(mttpl)

songdb={
    codename: {
    "artist": songdesc["COMPONENTS"][0]["Artist"],
    "assets": {
      "banner_bkgImageUrl": "",
      "coach1ImageUrl": "",
      "coach2ImageUrl": "",
      "coach3ImageUrl": "",
      "coach4ImageUrl": "",
      "coverImageUrl": "",
      "cover_1024ImageUrl": "",
      "cover_smallImageUrl": "",
      "expandBkgImageUrl": "",
      "expandCoachImageUrl": "",
      "phoneCoach1ImageUrl": "",
      "phoneCoach2ImageUrl": "",
      "phoneCoach3ImageUrl": "",
      "phoneCoach4ImageUrl": "",
      "phoneCoverImageUrl": "",
      "videoPreviewVideoURL": "",
      "map_bkgImageUrl": ""
    },
    "audioPreviewData": "{\"__class\":\"MusicTrackData\",\"structure\":{\"__class\":\"MusicTrackStructure\",\"markers\":"+str(mt["COMPONENTS"][0]["trackData"]["structure"]["markers"])+",\"signatures\":[{\"__class\":\"MusicSignature\",\"marker\":0,\"beats\":4}],\"startBeat\":"+str(mt["COMPONENTS"][0]["trackData"]["structure"]["startBeat"])+",\"endBeat\":"+str(mt["COMPONENTS"][0]["trackData"]["structure"]["endBeat"])+",\"fadeStartBeat\":0,\"useFadeStartBeat\":false,\"fadeEndBeat\":0,\"useFadeEndBeat\":false,\"videoStartTime\":"+str(mt["COMPONENTS"][0]["trackData"]["structure"]["videoStartTime"])+",\"previewEntry\":"+str(mt["COMPONENTS"][0]["trackData"]["structure"]["previewEntry"])+",\"previewLoopStart\":"+str(mt["COMPONENTS"][0]["trackData"]["structure"]["previewLoopStart"])+",\"previewLoopEnd\":"+str(mt["COMPONENTS"][0]["trackData"]["structure"]["previewLoopEnd"])+",\"volume\":"+str(mt["COMPONENTS"][0]["trackData"]["structure"]["volume"])+",\"fadeInDuration\":0,\"fadeInType\":0,\"fadeOutDuration\":0,\"fadeOutType\":0},\"path\":\"\",\"url\":\"jmcs://jd-contents/"+codename+"/"+codename+"_AudioPreview.ogg\"}",
    "coachCount": songdesc["COMPONENTS"][0]["NumCoach"],
    "credits": songdesc["COMPONENTS"][0]["Credits"],
    "difficulty": songdesc["COMPONENTS"][0]["Difficulty"],
    "doubleScoringType": -1,
    "jdmAttributes": [],
    "lyricsColor": str(matplotlib.colors.to_hex(songdesc["COMPONENTS"][0]["DefaultColors"]["lyrics"],keep_alpha = True).replace("#","").replace("ff","").upper())+"FF",
    "lyricsType": songdesc["COMPONENTS"][0]["LyricsType"],
    "mainCoach": songdesc["COMPONENTS"][0]["MainCoach"],
    "mapLength": 158.45,
    "mapName": codename,
    "mode": 6,
    "originalJDVersion": songdesc["COMPONENTS"][0]["OriginalJDVersion"],
    "packages": {
      "mapContent": codename+"_mapContent"
    },
    "parentMapName": codename,
    "skuIds": [],
    "songColors": {
      "songColor_1A": str(matplotlib.colors.to_hex(songdesc["COMPONENTS"][0]["DefaultColors"]["songcolor_1a"],keep_alpha = True).replace("#","").replace("ff","").upper())+"FF",
      "songColor_1B": str(matplotlib.colors.to_hex(songdesc["COMPONENTS"][0]["DefaultColors"]["songcolor_1b"],keep_alpha = True).replace("#","").replace("ff","").upper())+"FF",
      "songColor_2A": str(matplotlib.colors.to_hex(songdesc["COMPONENTS"][0]["DefaultColors"]["songcolor_2a"],keep_alpha = True).replace("#","").replace("ff","").upper())+"FF",
      "songColor_2B": str(matplotlib.colors.to_hex(songdesc["COMPONENTS"][0]["DefaultColors"]["songcolor_2b"],keep_alpha = True).replace("#","").replace("ff","").upper())+"FF"
    },
    "status": songdesc["COMPONENTS"][0]["Status"],
    "sweatDifficulty": songdesc["COMPONENTS"][0]["Difficulty"],
    "tags": songdesc["COMPONENTS"][0]["Tags"],
    "title": songdesc["COMPONENTS"][0]["Title"],
    "urls": {
      "jmcs://jd-contents/"+codename+"/"+codename+"_AudioPreview.ogg": "",
      "jmcs://jd-contents/"+codename+"/"+codename+"_MapPreviewNoSoundCrop_HIGH.vp8.webm": "",
      "jmcs://jd-contents/"+codename+"/"+codename+"_MapPreviewNoSoundCrop_HIGH.vp9.webm": "",
      "jmcs://jd-contents/"+codename+"/"+codename+"_MapPreviewNoSoundCrop_LOW.vp8.webm": "",
      "jmcs://jd-contents/"+codename+"/"+codename+"_MapPreviewNoSoundCrop_LOW.vp9.webm": "",
      "jmcs://jd-contents/"+codename+"/"+codename+"_MapPreviewNoSoundCrop_MID.vp8.webm": "",
      "jmcs://jd-contents/"+codename+"/"+codename+"_MapPreviewNoSoundCrop_MID.vp9.webm": "",
      "jmcs://jd-contents/"+codename+"/"+codename+"_MapPreviewNoSoundCrop_ULTRA.vp8.webm": "",
      "jmcs://jd-contents/"+codename+"/"+codename+"_MapPreviewNoSoundCrop_ULTRA.vp9.webm": ""
    },
    "searchTags": [],
    "searchTagsLocIds": [],
    "serverChangelist": 0
  }
}

contentauthdb={
  "__class": "ContentAuthorizationEntry",
    "duration": 300,
    "changelist": 280634,
    "urls": {
        "jmcs://jd-contents/"+codename+"/"+codename+"_ULTRA.webm": "",
        "jmcs://jd-contents/"+codename+"/"+codename+"_ULTRA.hd.webm": "",
        "jmcs://jd-contents/"+codename+"/"+codename+"_MID.webm": "",
        "jmcs://jd-contents/"+codename+"/"+codename+"_MID.hd.webm": "",
        "jmcs://jd-contents/"+codename+"/"+codename+"_LOW.webm": "",
        "jmcs://jd-contents/"+codename+"/"+codename+"_LOW.hd.webm": "",
        "jmcs://jd-contents/"+codename+"/"+codename+"_HIGH.webm": "",
        "jmcs://jd-contents/"+codename+"/"+codename+"_HIGH.hd.webm": "",
        "jmcs://jd-contents/"+codename+"/"+codename+".ogg": ""
    }
}

skudb={
  codename+"_mapContent": {
        "md5": "",
        "storageType": 0,
        "url": "",
        "version": 1
    }
}

json.dump(songdb,open(codenamelow+"_songdb.json","w"))
json.dump(skudb,open(codenamelow+"_skudb.json","w"))
json.dump(contentauthdb,open(codenamelow+"_mapdb.json","w"))
