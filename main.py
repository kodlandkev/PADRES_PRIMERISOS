import discord
from discord.ext import commands
from model import get_class
import requests

intents = discord.Intents.default()
intents.message_content=True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Hola nos hemos logueado con la cuenta llamada{bot.user}')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
            clas = get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}")[0]
            if clas == "golden\n":
                #dieta
                await ctx.send("Un canino detectado de la raza golden,tienen una dieta opta por fuentes magras como pollo, pavo, pescado y carne magra de ternera.")  
                #higiene
                await ctx.send("La higiene de este amigo peludo se recomienda cepillarlo 1 vez a la semana y bañar mensualmente.")
                #ejercicio
                await ctx.send("Tambien debemos evitar el ejercicio excesivo, los saltos, las caídas, los paseos muy largos y extenuarlo con juegos y carreras.")
                #dato curioso
                await ctx.send("Un dato curioso es que son una raza muy versátil que puede realizar diferentes trabajos, como búsqueda y rescate, asistencia a personas con discapacidad, obediencia, agilidad y guía. ")
            if clas == "dalmata\n":
                #dieta
                await ctx.send("Peludo detectado de la raza dalmata,tienen una dieta libres de purinas (carnes rojas, carne de res o pescado azul); el pollo, cordero, el pavo y parecidas, son carnes muy correctas para esta raza.")
                #higiene
                await ctx.send("La higiene de este perro vaca se puede vasar por su pelaje que es corto y de una sola capa. Por lo tanto, no es necesario cepillarlo a diario. Unas cuantas veces a la semana con un guante de goma es suficiente")
                #ejercicio
                await ctx.send("En el ejercicio se recomiendan más de dos horas diario en la edad adulta para que el perro esté en forma, además de adiestramiento y juegos para estimularles cuerpo y mente.")
                #dato curioso
                await ctx.send("Al nacer, los dálmatas son blancos y las manchas aparecen en las semanas siguientes. ")
            if clas == "pug\n":
                #dieta
                await ctx.send("Cachoro detectado de la raza pug,tienen una dieta la cual las porciones varían de acuerdo con el peso y la actividad física del pug, pero se recomienda administrar entre 120 y 150 gramos de carne (o pescado), de 10 a 30 gramos de cereales como arroz y entre 20 y 30 gramos de frutas y verduras.")
                #higiene
                await ctx.send("Para mantener brillante su pelaje, bastará con que le cepilles una vez por semana. En lo que respecta a su higiene, también es importante que te asegures de limpiarle los pliegues de la cara para evitar posibles infecciones. Por último, no olvides revisar las orejas y los ojos de manera periódica.")
                #ejercicio
                await ctx.send("Es muy importante que salga a pasear unas 3 veces al día y los paseos duren, al menos, 30 minutos.")
                #dato curioso
                await ctx.send("El nombre Pug podría venir de la expresión facial del perro, que se parece a la del mono tití. ")
            if clas == "brit\n":
                #dieta
                await ctx.send("Gato detectado de la raza british shorthair,tienen una dieta que debe incluir pienso seco, comida húmeda, y otros alimentos como la malta, la hierba de gato y el catnip.")
                #higiene
                await ctx.send("El pelo denso y suave necesita poco cepillado, como mucho una vez por semana.")
                #ejercicio
                await ctx.send("El ejercicio para un gato British Shorthair debe ser frecuente y entretenido para mantenerlo en forma y saludable. Se recomienda jugar con él a diario para desarrollar un vínculo fuerte.")
                #dato curioso
                await ctx.send("Mudan pelo estacionalmente durante la primavera y el otoño. ")
            if clas == "maine\n":
                #dieta
                await ctx.send("Gatuno detectado de la raza maine coon,tienen una dieta fácil que puede comer de todo: carne o pescado integrados en una ración completa y equilibrada, croquetas (de buena calidad). Recuerda que su dieta ha de estar siempre basada fundamentalmente en las proteínas animales. ")
                #higiene
                await ctx.send("Usa un peine de metal una vez a la semana para cepillar a tu gato y evitar que se formen nudos.")
                #ejercicio
                await ctx.send("20-60 minutos al día divididos en segmentos de 10 minutos.")
                #dato curioso
                await ctx.send("Los machos pueden pesar entre 6.8 y 11 kg, mientras que las hembras suelen pesar entre 4.5 y 6.8 kg. ")
            if clas == "siames\n":
                #dieta
                await ctx.send("Michi detectado de la raza siames,tienen una dieta que debe ser equilibrada, rica y variada, y debe incluir una combinación de pienso seco y húmedo de alta calidad.")
                #higiene
                await ctx.send("Esta raza es limpia y meticulosa en su higiene diaria. Te bastará con mantener limpia su bandeja sanitaria y estar atento al estado general de tu gato Siamés, así como desparasitarlo, vacunarlo y ofrecerle un rascador para que se afile las uñas.")
                #ejercicio
                await ctx.send("Necesita sesiones de juego diarias que estimulen su deseo natural de cazar y explorar . ")
                #dato curioso
                await ctx.send("Son muy leales a su familia y su carácter se asemeja al de un perro.")
            if clas == "beta\n":
                #dieta
                await ctx.send("Pez detectado de la raza beta,su dieta debe ser variada y completa, con alimentos vivos y comerciales insectos, gusanos, mosquitos y larvas y huevos de insectos ")
                #higiene
                await ctx.send("Cambia el agua semanalmente, Utilizar un filtro y cambiarlo periódicamente, Desinfectar la pecera con vinagre blanco. ")
                #origen
                await ctx.send("Los peces betta son originarios del sudeste asiático y viven en charcas, arrozales, planicies inundadas y otras formaciones de agua estancada o con movimiento lento.")
                #dato curioso
                await ctx.send("Son grandes saltadores y nadadores, por lo que es importante que su pecera tenga tapa para que no salgan. ")
            if clas == "payaso\n":
                #dieta
                await ctx.send("Su dieta es omnívora, es decir, debe incluir alimentos de origen animal y vegetal.")
                #higiene
                await ctx.send("Mantener el agua limpia, limpiar y cambiar los filtros; sacar los restos de algas y, si muere algún pez, retirarlo inmediatamente. ")
                #origen
                await ctx.send("Son originarios de la zona Indo-Pacífica, en aguas poco profundas del océano Índico, el mar Rojo y el Pacífico occidental.")
                #dato curioso
                await ctx.send("Todos nacen como machos y algunos se convierten en hembras más adelante en su vida.")
            if clas == "angel\n":
                #dieta
                await ctx.send("Alimentos en escamas, congelados, liofilizados y vivos 2 a 3 veces al día y retirar cualquier resto de alimento para reducir los desechos.")
                #higiene
                await ctx.send("El acuario debe ser de tamaño grande, con una capacidad de, al menos, 55 litros por cada pez ángel. También es importante colocar plantas naturales dentro del acuario para oxigenar el agua, eliminar contaminantes y proporcionar lugares donde los peces puedan ocultarse. ")
                #origen
                await ctx.send("Son originarios de la cuenca del Amazonas, la cuenca del Orinoco y varios ríos del Escudo Guayanés en la zona tropical de América del Sur. ")
                #dato curioso
                await ctx.send("Son peces óseos con un esqueleto interno que les permite controlar con precisión el movimiento de sus aletas. ")
    else:
        await ctx.send("no has subido ninguna imagen")

    
bot.run('TOKEN')
