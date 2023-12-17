import requests
class Client():
	def __init__(self):
		self.headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","x-requested-with": "XMLHttpRequest"}
		self.api='https://anitype.site'
	def send_code(self,email):
	    data={"redirect":"https://anitype.fun/auth/email","email":email}
	    return requests.post(f"{self.api}/app2/auth/email/send",json=data,headers=self.headers)
	def login(self,code):
	    data={"code":code}
	    req=requests.post(f"{self.api}/app2/auth/email/login",json=data,headers=self.headers).json()
	    self.headers['Authorization']=f"req['type']req['accessToken']"
	    return req
	def status(self):
	    return requests.get(f"https://anitype.site/dj/recs/status",headers=self.headers).json()
	def search(self,keyword):
	    return requests.get(f"{self.api}/anime/search?keyword={keyword}",headers=self.headers).json()
	def selections(self,title,description:str=None):
	    data={"title":title,"description":description}
	    return requests.post(f"{self.api}/app2/selections",json=data,headers=self.headers).json()
	def releases_selections(self,review,releaseId,selectionId):
	    data={"selectionId":selectionId,"releaseId":releaseId,"review":review}
	    return requests.post(f"{self.api}/app2/selections/releases",json=data,headers=self.headers).json()
	def rates_post(self):
	    data={"anime_id":anime_id,"value":value}
	    return requests.post(f"{self.api}/dj/rates/auth/",json=data,headers=self.headers).json()
	def add_folders(self,releaseId,folderTitle:str="Буду смотреть",base:str="anime"):
	    data={"folderTitle":folderTitle,"releaseId":releaseId,"base":base}
	    return requests.post(f"{self.api}/app2/folders/add",json=data,headers=self.headers).json()
	def anime_info(self,anime_id):
	    return requests.get(f"{self.api}/anime/ids?ids={anime_id}",headers=self.headers).json()
	def submit_comment(self,text,releaseId,hasSpoiler:bool=False):
	    data={"value":text,"releaseId":releaseId,"hasSpoiler":hasSpoiler}
	    return requests.post(f"{self.api}/app2/comments",json=data,headers=self.headers).json()
	def notification_list(self,page,size):
	    return requests.get(f"{self.api}/app2/notifications?page={page}&size={size}",headers=self.headers).json()