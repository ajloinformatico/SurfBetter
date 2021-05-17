from models import User, Beach, DesciptionPoints
from extensions import db, guard
import os

def seed(app):
    """
    Make seeder if it is necessary
    """
    with app.app_context():
        db.create_all()
        if db.session.query(User).filter_by(email="ajloinformatico@gmail.com").count() < 1:
            db.session.add(
                User(
                    email="ajloinformatico@gmail.com",
                    name="Infolojo",
                    surname="Infolojo",
                    nick="@infolojo",
                    password=guard.hash_password("pestillo01"),
                    roles="admin",
                )
            )
            db.session.commit()

            # Create user directory
            if not os.path.isdir("statics/user/@infolojo"):
                os.makedirs("statics/user/@infolojo")

        # Beaches seeder
        if db.session.query(Beach).count() < 1:
            db.session.add(
                Beach(
                    name = "La muralla",
                    image = "/statics/beaches/la_muralla/playa_de_la_muralla_1.jpg",
                    description = "La Muralla in Andalucia is a quite exposed reef break " 
                        +"that has fairly consistent surf. Winter and spring are the optimum " 
                        +"times of year to visit. Offshore winds are from the north. Tends to "
                        +"receive a mix of groundswells and windswells and the best swell direction "
                        +"is from the southwest. A right hand reef. Best around mid tide when the tide "
                        +"is rising. It's often crowded here. Watch out for rocks.",
                    type="Reef",
                    flag=3,
                    quality_when_it_works = 3,
                    wave_consistency = 3,
                    difficulty = 2,
                    windsurf_y_kitesurf = 1,
                    people_to_Water = 4,
                    sea_weends = 3,
                    other_options = 2,
                    water_quality = 3,
                    access = 5, 
                    scenery = 3,
                    local_attitude = 5,
                    accommodation = 5,
                    camping = 3,
                    entertainment = 5,
                    equipment_and_repairs = 2, 
                    restaurants = 5,
                    pubs = 5
                ),
                Beach(
                    name = "Las Redes",
                    image = "/statics/beaches/la_muralla/playa_de_las_redes_1.jpg",
                    description = "Las Redes in Andalucia is a reasonably exposed beach "
                    +"break that has pretty consitent surf. Winter and spring are the best "
                    +"times of year to visit. Offshore winds are from the north northeast. "
                    +"Tends to receive a mix of groundswells and windswells and the ideal swell "
                    +"direction is from the west southwest. Waves at the beach are both lefts and "
                    +"rights. Best around mid tide when the tide is rising. When the surf is up, it "
                    +"can get quite busy in the water. It can even get crowded enough to be dangerous.",
                    type = "Sandbar",
                    flag = 3,
                    quality_when_it_works = 3,
                    wave_consistency = 2,
                    difficulty = 3,
                    windsurf_y_kitesurf = 4,
                    people_to_Water = 3,
                    sea_weends = 4,
                    other_options = 4,
                    water_quality = 3,
                    access = 5,
                    scenery = 2,
                    local_attitude = 3,
                    accommodation = 5,
                    camping = 3,
                    entertainment = 5,
                    equipment_and_repairs = 5,
                    restaurants = 4,
                    pubs = 5
                ),
                Beach(
                    name = "La Playita",
                    image = "/statics/beaches/la_playita/la_playita_1.jpg",
                    description = "La Playita in Andalucia is an exposed beach break that has reasonably consistent surf. "
                    +"Winter and spring are the optimum times of year to visit. Ideal winds are from the northeast. Tends " 
                    +"to receive a mix of groundswells and windswells and the best swell direction is from the southwest. "
                    +"Waves at the beach break both left and right. A popular wave that can get growded. Watch out for rocks.",
                    type = "Beach",
                    flag = 1,
                    quality_when_it_works = 3,
                    wave_consistency = 3,
                    difficulty = 3,
                    windsurf_y_kitesurf = 1,
                    people_to_Water = 2,
                    sea_weends = 4,
                    other_options = 4,
                    water_quality = 3,
                    access = 5,
                    scenery = 3,
                    local_attitude = 5,
                    accommodation = 3,
                    camping = 3,
                    entertainment = 4,
                    equipment_and_repairs = 4,
                    restaurants = 3,
                    pubs = 3
                ),
                """
                Beach(
                    name = "Las Caracolas",
                    image = "/statics/beaches/la_playita/las_caracolas_1.jpg",
                    description = "Las Caracolas in Andalucia is an exposed beach "
                    +"and reef break that has fairly consistent surf. Winter and spring "
                    +"are the best times of year to visit. The best wind direction is "
                    +"from the northeast. Most of the surf here comes from groundswells "
                    +"and the ideal swell direction is from the southwest. Waves at the beach "
                    +"break both left and right. Best around mid tide. Likely to be crowded if working. Watch out for rocks. ",
                    +"",
                )
                """
            )
            db.session.commit()

        if db.session.query(DesciptionPoints).count() < 1:
            db.session.add(
                DesciptionPoints(
                    name = "Quality when ir works",
                    description = "(1: Even with a perfect swell and wind, the waves are not good. 5: With good conditions, the waves will be world class)."
                ),
                DesciptionPoints(
                    name = "Wave consistency",
                    description = "(1: La Muralla is a fickle surf spot that only works a few times a year. 5: Reliable year-round spot)."
                ),
                DesciptionPoints(
                    name = "Difficulty",
                    description = "(1: Bien para principiantes. 3: Intermedios. 5: Sólo Surfistas Expertos)."
                ),
                DesciptionPoints(
                    name = "Windsurf y kitesurf",
                    description = "(1: An unsuitable location. 5: The wind and swell at La Muralla are often excellent)."
                ),
                DesciptionPoints(
                    name = "Access",
                    description = "(1: Llegar a La Muralla requiere una expedición por tierra o alquiler un barco. 3: Una caminata de 30 minutos desde el aparcamiento más cercano. 5: Aparcamiento en frente del Spot)."
                ),
                DesciptionPoints(
                    name = "Scenery",
                    description = "(1: Un paisaje industrial horrible. 5: Un paisaje espectacular)."
                ),
                DesciptionPoints(
                    name = "Local attitude",
                    description = "(1: Surfistas locales no les gustan visitantes. 5: No hay surfistas locales, o si hay, son hospitalarios y amables)."
                ),
                DesciptionPoints(
                    name = "Accommodation",
                    description = "(1: No accommodation. 5: Many accommodation options near La Muralla for all budgets from hostels to luxury hotels)."
                ),
                DesciptionPoints(
                    name = "Camping",
                    description = "(1: No es posible acampar en La Muralla. 3: Es posible acampar, pero no hay instalaciones. 5: Una campismo cercana que cuenta con excelentes instalaciones y buena onda)."
                ),
                DesciptionPoints(
                    name = "Entertainment",
                    description = "(1: Aparte del surf y la soledad no hay nada que hacer cuando no hay olas. 5: La Muralla es localizado una región muy interesante, surfear allí es un bono)."
                ),
                DesciptionPoints(
                    name = "Equipment and repairs",
                    description = "(1: No se puede comprar nada, ni siquiera wax. 5: Equipamiento de surf de calidad para compra o alquiler con reparaciones disponibles)."
                ),
                DesciptionPoints(
                    name = "Restaurants",
                    description = "(1: Traer su propia comida, ni siquiera hay una tienda. 5: Muchos distintos restaurantes y bares en La Muralla, desde comida rápida a restaurantes de lujo)."
                ),
                DesciptionPoints(
                    name = "Pubs",
                    description = "(1: El alcohol está prohibido en el país. 5: Hay un bar excelente, cerca de La Muralla donde puedes aparcar la furgoneta para la noche)."
                )
            )
            db.session.commit()

                
