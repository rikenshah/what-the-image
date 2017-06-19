# What The Image !!!

In this project, the main object in the uploaded image is identified. Along with the image identification, the system also provides a short description of the identified object.
The project is hosted here : [What the image](http://whattheimage.herokuapp.com/) 

### How it works 
1. User uploads an image :

![normal](https://raw.githubusercontent.com/rikenshah/what-the-image/master/screenshots/one.png)

The uploaded image :
![normal](https://raw.githubusercontent.com/rikenshah/what-the-image/master/teapot.png)

2. The results :

![normal](https://raw.githubusercontent.com/rikenshah/what-the-image/master/screenshots/two.png)

3. To see description of the object, user clicks on _View Description_ :

![normal](https://raw.githubusercontent.com/rikenshah/what-the-image/master/screenshots/three.png)

### Technologies used : 
1. _Django_ : Django is a python's framework for developing web applications. To know more about Django, visit here [Django documentation](https://docs.djangoproject.com/en/1.11/)

2. _ImageNet_ : Image net is an easliy accessible image database. It is built according to the wordnet hierarchy. ImageNet only provides thumbnails and URLs of images, in a way similar to what image search engines do. For more on ImageNet, visit here [ImageNet](http://www.image-net.org/download-API)

3. _TensorFlow_ : TensorFlow is a Google's Deep learning framework using Python. A trained Image model of TensorFlow has been used in out project.

4. _DuckDuckGo_ : DuckDuckGo is a search engine. The idenfied object is searched by the DuckDuckGo API and the results are scraped to get the final description. This piece of code gets the description :
```python
class duckduckGo(object):
	
	def getInfo(self,nameOfTopic):
		url = "https://api.duckduckgo.com/?q="+nameOfTopic+"&format=json&pretty=1&no_html=1&skip_disambig=1"
		r = requests.get(url)
		data = r.json()
		print data['AbstractText']
		return data['AbstractText']
```
[DuckDuckGo Documentation](https://duckduckgo.com/api)
