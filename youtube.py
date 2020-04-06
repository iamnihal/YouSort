import requests
import csv
import json

#Globally declared list to avoid overwriting of data.
ratio = []
video = []
title = []
like = []
dislike = []

def myfunction():
    global COUNTRY
    COUNTRY = input("Enter your ISO alpha-2 country code (If don't know, type Enter):- ")
    if (len(COUNTRY) != 2) or (not COUNTRY):
        cCode = """Name,Code
        Afghanistan,AF
        aland Islands,AX
        Albania,AL
        Algeria,DZ
        American Samoa,AS
        Andorra,AD
        Angola,AO
        Anguilla,AI
        Antarctica,AQ
        Antigua and Barbuda,AG
        Argentina,AR
        Armenia,AM
        Aruba,AW
        Australia,AU
        Austria,AT
        Azerbaijan,AZ
        Bahamas,BS
        Bahrain,BH
        Bangladesh,BD
        Barbados,BB
        Belarus,BY
        Belgium,BE
        Belize,BZ
        Benin,BJ
        Bermuda,BM
        Bhutan,BT
        "Bolivia, Plurinational State of",BO
        "Bonaire, Sint Eustatius and Saba",BQ
        Bosnia and Herzegovina,BA
        Botswana,BW
        Bouvet Island,BV
        Brazil,BR
        British Indian Ocean Territory,IO
        Brunei Darussalam,BN
        Bulgaria,BG
        Burkina Faso,BF
        Burundi,BI
        Cambodia,KH
        Cameroon,CM
        Canada,CA
        Cape Verde,CV
        Cayman Islands,KY
        Central African Republic,CF
        Chad,TD
        Chile,CL
        China,CN
        Christmas Island,CX
        Cocos (Keeling) Islands,CC
        Colombia,CO
        Comoros,KM
        Congo,CG
        "Congo, the Democratic Republic of the",CD
        Cook Islands,CK
        Costa Rica,CR
        Cate d'Ivoire,CI
        Croatia,HR
        CubaCU
        Curaaaao,CW
        Cyprus,CY
        Czech Republic,CZ
        Denmark,DK
        Djibouti,DJ
        Dominica,DM
        Dominican Republic,DO
        Ecuador,EC
        Egypt,EG
        El Salvador,SV
        Equatorial Guinea,GQ
        Eritrea,ER
        Estonia,EE
        Ethiopia,ET
        Falkland Islands (Malvinas),FK
        Faroe Islands,FO
        Fiji,FJ
        Finland,FI
        France,FR
        French Guiana,GF
        French Polynesia,PF
        French Southern Territories,TF
        Gabon,GA
        Gambia,GM
        Georgia,GE
        Germany,DE
        Ghana,GH
        Gibraltar,GI
        Greece,GR
        Greenland,GL
        Grenada,GD
        Guadeloupe,GP
        Guam,GU
        Guatemala,GT
        Guernsey,GG
        Guinea,GN
        Guinea-Bissau,GW
        Guyana,GY
        Haiti,HT
        Heard Island and McDonald Islands,HM
        Holy See (Vatican City State),VA
        Honduras,HN
        Hong Kong,HK
        Hungary,HU
        Iceland,IS
        India,IN
        Indonesia,ID
        "Iran, Islamic Republic of",IR
        Iraq,IQ
        Ireland,IE
        Isle of Man,IM
        Israel,IL
        Italy,IT
        Jamaica,JM
        Japan,JP
        Jersey,JE
        Jordan,JO
        Kazakhstan,KZ
        Kenya,KE
        Kiribati,KI
        "Korea, Democratic People's Republic of",KP
        "Korea, Republic of",KR
        Kuwait,KW
        Kyrgyzstan,KG
        Lao People's Democratic Republic,LA
        Latvia,LV
        Lebanon,LB
        Lesotho,LS
        Liberia,LR
        Libya,LY
        Liechtenstein,LI
        Lithuania,LT
        Luxembourg,LU
        Macao,MO
        "Macedonia, the Former Yugoslav Republic of",MK
        Madagascar,MG
        Malawi,MW
        Malaysia,MY
        Maldives,MV
        Mali,ML
        Malta,MT
        Marshall Islands,MH
        Martinique,MQ
        Mauritania,MR
        Mauritius,MU
        Mayotte,YT
        Mexico,MX
        "Micronesia, Federated States of",FM
        "Moldova, Republic of",MD
        Monaco,MC
        Mongolia,MN
        Montenegro,ME
        Montserrat,MS
        Morocco,MA
        Mozambique,MZ
        Myanmar,MM
        Namibia,NA
        Nauru,NR
        Nepal,NP
        Netherlands,NL
        New Caledonia,NC
        New Zealand,NZ
        Nicaragua,NI
        Niger,NE
        Nigeria,NG
        Niue,NU
        Norfolk Island,NF
        Northern Mariana Islands,MP
        Norway,NO
        Oman,OM
        Pakistan,PK
        Palau,PW
        "Palestine, State of",PS
        Panama,PA
        Papua New Guinea,PG
        Paraguay,PY
        Peru,PE
        Philippines,PH
        Pitcairn,PN
        Poland,PL
        Portugal,PT
        Puerto Rico,PR
        Qatar,QA
        Romania,RO
        Russian Federation,RU
        Rwanda,RW
        "Saint Helena, Ascension and Tristan da Cunha",SH
        Saint Kitts and Nevis,KN
        Saint Lucia,LC
        Saint Martin (French part),MF
        Saint Pierre and Miquelon,PM
        Saint Vincent and the Grenadines,VC
        Samoa,WS
        San Marino,SM
        Sao Tome and Principe,ST
        Saudi Arabia,SA
        Senegal,SN
        Serbia,RS
        Seychelles,SC
        Sierra Leone,SL
        Singapore,SG
        Sint Maarten (Dutch part),SX
        Slovakia,SK
        Slovenia,SI
        Solomon Islands,SB
        Somalia,SO
        South Africa,ZA
        South Georgia and the South Sandwich Islands,GS
        South Sudan,SS
        Spain,ES
        Sri Lanka,LK
        Sudan,SD
        Suriname,SR
        Svalbard and Jan Mayen,SJ
        Swaziland,SZ
        Sweden,SE
        Switzerland,CH
        Syrian Arab Republic,SY
        "Taiwan, Province of China",TW
        Tajikistan,TJ
        "Tanzania, United Republic of",TZ
        Thailand,TH
        Timor-Leste,TL
        Togo,TG
        Tokelau,TK
        Tonga,TO
        Trinidad and Tobago,TT
        Tunisia,TN
        Turkey,TR
        Turkmenistan,TM
        Turks and Caicos Islands,TC
        Tuvalu,TV
        Uganda,UG
        Ukraine,UA
        United Arab Emirates,AE
        United Kingdom,GB
        United States,US
        United States Minor Outlying Islands,UM
        Uruguay,UY
        Uzbekistan,UZ
        Vanuatu,VU
        "Venezuela, Bolivarian Republic of",VE
        Viet Nam,VN
        "Virgin Islands, British",VG
        "Virgin Islands, U.S.",VI
        Wallis and Futuna,WF
        Western Sahara,EH
        Yemen,YE
        Zambia,ZM
        Zimbabwe,ZW"""
        print("Here's country code list: \n" + cCode)
        conn = myfunction()
        return conn
    else:
        return COUNTRY


def infoExtract(URL):

    response = requests.get(URL)
    response_json = response.json()
    first = response_json['items']

    #Video ID
    for id in first:
        video.append(id['id'])

    #Adding video id to base url
    string = "https://www.youtube.com/watch?v="
    video_id = ["{}{}".format(string,i) for i in video ]

    #Video Title
    for t in first:
        title.append(t['snippet']['title'])

    #Like
    for l in first:
        like.append(int(l['statistics'].get('likeCount',0)))

    #Dislike
    for d in first:
        dislike.append(int(d['statistics'].get('dislikeCount',0)))

    #NextPageToken
    pagetoken = response_json.get('nextPageToken',None)
    if (pagetoken == None):

        #Creating a list of ratio
        for e1, e2 in zip(like, dislike):
            try:
                result = e1 / e2
                ratio.append(round(result,2))
            except ZeroDivisionError:
                result = 0
                ratio.append(result)

        #Creating a final list of tuples having ratio, title, video_id as an element(tuples) of list.
        z = list(zip(ratio, title, video_id))

        #Sortig list w.r.t to 1 key(Rating) in the tuples.
        z.sort(key = lambda x: x[0], reverse = True)

        #Writing final result to trend.csv file
        with open('trend.csv','a+') as out:
            csv_out=csv.writer(out)
            csv_out.writerows(z)
        return
    else:
        nextPage = "https://www.googleapis.com/youtube/v3/videos?part=id,statistics,                                                            snippet&chart=mostPopular&regionCode={}&maxResults=50&pageToken={}&key=AIzaSyC5raPdl86CoqrvLRnGL41uzo0aHWFxBsg".format(conn,pagetoken)
        infoExtract(nextPage)

conn = myfunction()
initURL = "https://www.googleapis.com/youtube/v3/videos?part=id,statistics,                                                            snippet&chart=mostPopular&regionCode={}&maxResults=50&key=AIzaSyC5raPdl86CoqrvLRnGL41uzo0aHWFxBsg".format(conn)

infoExtract(initURL)
