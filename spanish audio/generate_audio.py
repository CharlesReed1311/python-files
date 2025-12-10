from gtts import gTTS

spanish_text = """
Hola, me llamo Chaitanya y hoy quiero hablarles sobre mi película favorita: In Time.
Esta película me atrapó desde el primer momento, no solo por su trama original,
sino por las preguntas profundas que plantea sobre la vida, el tiempo y la desigualdad.

In Time está ambientada en un futuro donde el tiempo es literalmente dinero.
Las personas dejan de envejecer a los 25 años, pero a partir de ahí,
tienen que ganarse cada segundo de vida. Si el tiempo se acaba, mueren.
Imagínense vivir así, mirando constantemente un reloj en tu brazo que marca cuánto te queda de vida.

Lo que más me impacta es cómo la película refleja la realidad de nuestra sociedad.
Hay personas que viven al día, luchando por sobrevivir, mientras otros tienen siglos en sus relojes,
viviendo con lujos y sin preocupaciones. Es una crítica muy clara al sistema económico actual
y a la desigualdad entre ricos y pobres.

El protagonista, interpretado por Justin Timberlake, es un hombre del gueto que recibe una gran cantidad de tiempo
y decide usarlo para luchar contra el sistema. Me encanta cómo su personaje evoluciona:
pasa de simplemente querer sobrevivir a querer cambiar el mundo.

Además, la idea de que el tiempo es la moneda más valiosa nos hace reflexionar sobre cómo usamos el nuestro.
¿Lo desperdiciamos? ¿Lo valoramos lo suficiente? In Time me hizo pensar mucho sobre eso.

En resumen, esta película no es solo ciencia ficción, es una reflexión profunda disfrazada de acción.
Y por eso, In Time es mi película favorita.
"""

tts = gTTS(text=spanish_text, lang='es')
tts.save("monologo_in_time_es_chaitanya.mp3")
print("✅ Audio file 'monologo_in_time_es_chaitanya.mp3' created successfully!")
