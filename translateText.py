'''
2022.04.19 이동한
goslate는 백엔드에서 Google 번역기 API를 사용함
goslate 구글 번역사이트를 쿼리하여 제공
'''
import goslate
text = "Bonjour le monde"
gs = goslate.Goslate()
translatedText = gs.translate(text, 'en')
print(translatedText)

