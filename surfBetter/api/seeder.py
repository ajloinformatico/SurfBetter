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
                    pubs = 5,
                    surf_fore_cast_link = '<link href="//www.surf-forecast.com/stylesheets/widget.css" media="screen" rel="stylesheet" type="text/css" /><div class="wf-width-cont surf-fc-widget"><div class="widget-container"><div class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" src="//www.surf-forecast.com/breaks/La-Muralla/forecasts/widget/a" scrolling="no" frameborder="0" marginwidth="0" marginheight="0"></iframe></div></div></div>'
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
                    pubs = 5,
                    surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" media="screen" rel="stylesheet" type="text/css" /><div class="wf-width-cont surf-fc-widget"><div class="widget-container"><div class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" src="//www.surf-forecast.com/breaks/Las-Redes/forecasts/widget/a" scrolling="no" frameborder="0" marginwidth="0" marginheight="0"></iframe></div></div></div>'
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
                    pubs = 3,
                    surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" media="screen" rel="stylesheet" type="text/css" /><div class="wf-width-cont surf-fc-widget"><div class="widget-container"><div class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" src="//www.surf-forecast.com/breaks/Las-Caracolas/forecasts/widget/a" scrolling="no" frameborder="0" marginwidth="0" marginheight="0"></iframe></div></div></div>'
                ),
                Beach(
                    name = "Las Caracolas",
                    image = "/statics/beaches/la_playita/las_caracolas_1.jpg",
                    description = "Las Caracolas in Andalucia is an exposed beach "
                    +"and reef break that has fairly consistent surf. Winter and spring "
                    +"are the best times of year to visit. The best wind direction is "
                    +"from the northeast. Most of the surf here comes from groundswells "
                    +"and the ideal swell direction is from the southwest. Waves at the beach "
                    +"break both left and right. Best around mid tide. Likely to be crowded if working. Watch out for rocks. ",
                    type = "Beach and reef",
                    flag= 2,
                    quality_when_it_works = 3,
                    wave_consistency = 3,
                    difficulty = 2,
                    windsurf_y_kitesurf = 5,
                    people_to_Water = 3,
                    surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" media="screen" rel="stylesheet" type="text/css" /><div class="wf-width-cont surf-fc-widget"><div class="widget-container"><div class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" src="//www.surf-forecast.com/breaks/Las-Caracolas/forecasts/widget/a" scrolling="no" frameborder="0" marginwidth="0" marginheight="0"></iframe><div class="footer"><a class="logo" href="//www.surf-forecast.com/"><img src="//www.surf-forecast.com/images/widget.png" alt="Widget" width="1" height="1" /></a><div class="about" id="cmt">More <a href="//www.surf-forecast.com/breaks/Las-Caracolas">Detailed Surf Conditions &amp; Webcams for&nbsp;Las Caracolas</a> <nobr>at&nbsp;<a href="//www.surf-forecast.com/">surf-forecast.com</a></nobr>.</div></div></div></div></div>'
                ),
                Beach(
                    name = "la Cabanita",
                    image = "/statics/beaches/la_cabanita/la_cabanita_1.jpg",
                    description = "La Cabanita in Andalucia is an exposed reef "
                    +"break that only works when conditions are just right. Winter "
                    +"and spring are the best times of year to visit. Offshore winds "
                    +"are from the north northeast. Windswells and groundswells in equal "
                    +"measure and the ideal swell direction is from the west southwest. "
                    +"A right hand reef break. Good surf at all stages of the tide. Rarely "
                    +"crowded here. Submerged rocks are a hazard.",
                    type= "Beach",
                    flag = 2,
                    quality_when_it_works = 3,
                    wave_consistency = 2,
                    difficulty = 3,
                    windsurf_y_kitesurf = 2,
                    people_to_Water = 3,
                    sea_weends = 3,
                    other_options = 3,
                    water_quality = 3,
                    access = 5,
                    scenery = 2,
                    local_attitude = 2,
                    accommodation = 4,
                    camping = 4,
                    entertainment = 4,
                    equipment_and_repairs = 3,
                    restaurants = 4,
                    pubs = 3,
                    surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" media="screen" rel="stylesheet" type="text/css" /><div class="wf-width-cont surf-fc-widget"><div class="widget-container"><div class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" src="//www.surf-forecast.com/breaks/La-Cabanita/forecasts/widget/a" scrolling="no" frameborder="0" marginwidth="0" marginheight="0"></iframe></div></div></div>'
                ),
                Beach(
                    name="Torre Gorda",
                    image="/statics/beaches/torre_gorda/torre_gorda_1.jpg",
                    description="Torre Gorda in Andalucia is an exposed beach break that does not work very often. "
                    +"Winter and spring are the best times of year to visit. The best wind direction is from the "
                    +"east northeast. Tends to receive a mix of groundswells and windswells and the ideal swell "
                    +"direction is from the west. The beach breaks offer lefts and rights. Best around high tide. "
                    +"Rarely crowded here.",
                    type= "Beach",
                    flag = 3,
                    quality_when_it_works = 1,
                    wave_consistency = 2,
                    difficulty = 4,
                    windsurf_y_kitesurf = 3,
                    people_to_Water = 4,
                    surf_fore_cast_link = '<link href="//www.surf-forecast.com/stylesheets/widget.css" media="screen" rel="stylesheet" type="text/css" /><div class="wf-width-cont surf-fc-widget"><div class="widget-container"><div class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" src="//www.surf-forecast.com/breaks/Torre-Gorda/forecasts/widget/a" scrolling="no" frameborder="0" marginwidth="0" marginheight="0"></iframe></div></div></div>'
                ),
                Beach(
                    name = "Playa de Camposoto",
                    image = "/statics/beaches/playa_de_camposoto/playa_de_camposoto_1.jpg",
                    description = "Playa Campo Sota in Andalucia is an exposed beach break that "
                    +"has quite reliable surf. Winter and spring are the optimum times of year to visit. "
                    +"Ideal winds are from the east northeast. Windswells and groundswells in equal measure "
                    +"and the optimum swell angle is from the west southwest. The beach breaks offer lefts and "
                    +"rights. It's often crowded here.",
                    type = "Beach",
                    flag = 3,
                    quality_when_it_works = 3,
                    wave_consistency = 3,
                    difficulty = 3,
                    windsurf_y_kitesurf = 2,
                    people_to_Water = 3,
                    sea_weends = 3,
                    other_options = 3,
                    water_quality = 5,
                    access = 5,
                    scenery = 4,
                    local_attitude = 2,
                    accommodation = 2,
                    camping = 1,
                    entertainment = 3,
                    equipment_and_repairs = 2,
                    restaurants = 3,
                    pubs = 2,
                    surf_fore_cast_link = '<link href="//www.surf-forecast.com/stylesheets/widget.css" media="screen" rel="stylesheet" type="text/css" /><div class="wf-width-cont surf-fc-widget"><div class="widget-container"><div class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" src="//www.surf-forecast.com/breaks/Playa-Campo-Sota/forecasts/widget/a" scrolling="no" frameborder="0" marginwidth="0" marginheight="0"></iframe></div></div></div>',
                ),
                Beach(
                    name = "Chiclana de la frontera",
                    image= "/statics/beaches/chiclana_de_la_fromtera/chiclana_de_la_frontera_1.jpg",
                    description = "Chiclana de la Frontera in Andalucia is an "
                    +"exposed beach break that has inconsistent surf. Summer in "
                    +"particular tends to be flat. The best wind direction is from "
                    +"the east. Waves just as likely from local windswells as from "
                    +"distant groundswells and the ideal swell direction is from the "
                    +"southwest. The beach break provides left and right handers.",
                    type = "Beach",
                    flag = 3,
                    quality_when_it_works = 2,
                    wave_consistency = 2,
                    difficulty = 3,
                    windsurf_y_kitesurf = 1,
                    people_to_Water = 3,
                    water_quality = 3,
                    surf_fore_cast_link = '<link href="//www.surf-forecast.com/stylesheets/widget.css" media="screen" rel="stylesheet" type="text/css" /><div class="wf-width-cont surf-fc-widget"><div class="widget-container"><div class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" src="//www.surf-forecast.com/breaks/Chiclanadela-Frontera/forecasts/widget/a" scrolling="no" frameborder="0" marginwidth="0" marginheight="0"></iframe></div></div></div>'
                ),
                Beach(
                    name = "El Castillo",
                    image = "/statics/beaches/el_castillo/el_castillo_1.jpg",
                    description = "El Castillo in Andalucia is an exposed point break that has inconsistent "
                    +"surf. Winter is the best time of year for surfing here. Ideal winds are from the east "
                    +"southeast and there is no shelter here from cross shore breezes. Tends to receive a mix "
                    +"of groundswells and windswells and the best swell direction is from the west southwest. "
                    +"No point break here. Best around mid tide. Rarely crowded here. Rocks are a hazard.",
                    type = "Point",
                    flag = 2,
                    quality_when_it_works = 4,
                    wave_consistency = 3,
                    difficulty = 4,
                    windsurf_y_kitesurf = 1,
                    people_to_Water = 3,
                    sea_weends = 1,
                    other_options = 5,
                    water_quality = 5,
                    access = 3,
                    scenery = 4,
                    local_attitude = 4,
                    accommodation = 4,
                    camping = 3,
                    entertainment = 3,
                    equipment_and_repairs = 2,
                    restaurants = 4,
                    pubs = 1,
                    surf_fore_cast_link = '<link href="//www.surf-forecast.com/stylesheets/widget.css" media="screen" rel="stylesheet" type="text/css" /><div class="wf-width-cont surf-fc-widget"><div class="widget-container"><div class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" src="//www.surf-forecast.com/breaks/El-Castillo/forecasts/widget/a" scrolling="no" frameborder="0" marginwidth="0" marginheight="0"></iframe></div></div></div>'
                ),
                Beach(
                    name = "La Barrosa",
                    image = "/statics/beaches/el_castillo/el_castillo_1.jpg",
                    description = "La Barossa in Andalucia is an exposed beach "
                    +"break that has reasonably consistent surf, although summer "
                    +"tends to be mostly flat. Offshore winds are from the east "
                    +"northeast and there is no shelter here from cross shore breezes. "
                    +"Most of the surf here comes from groundswells and the best swell "
                    +"direction is from the west southwest. The beach break provides left "
                    +"and right handers. Good surf at all stages of the tide. Rarely crowded here. "
                    +"Beware of buoys, fishing nets,pollution.",
                    type = "Beach",
                    flag = 3,
                    quality_when_it_works = 3,
                    wave_consistency = 3,
                    difficulty = 2,
                    windsurf_y_kitesurf = 3,
                    people_to_Water = 4,
                    sea_weends = 2,
                    other_options = 2,
                    water_quality = 4,
                    access = 5,
                    scenery = 5,
                    local_attitude = 4,
                    accommodation = 5,
                    camping = 1,
                    entertainment = 5,
                    equipment_and_repairs = 1,
                    restaurants = 5,
                    pubs = 5,
                    surf_fore_cast_link = '<link href="//www.surf-forecast.com/stylesheets/widget.css" media="screen" rel="stylesheet" type="text/css" /><div class="wf-width-cont surf-fc-widget"><div class="widget-container"><div class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" src="//www.surf-forecast.com/breaks/La-Barossa/forecasts/widget/a" scrolling="no" frameborder="0" marginwidth="0" marginheight="0"></iframe></div></div></div>',
                ),
                Beach(
                    name = "Cabo Roche",
                    image = "/statics/beaches/cabo_roche/cabo_roche_1.jpg",
                    description = "Cabo Roche in Andalucia is an exposed beach break that has dependable "
                    +"surf. Winter and spring are the optimum times of year to visit. The best wind direction "
                    +"is from the east. Tends to receive a mix of groundswells and windswells and the best swell "
                    +"direction is from the southwest. Waves at the beach break both left and right. It's sometimes "
                    +"crowded here. Watch out for rocks.",
                    type = "Beach",
                    flag = 2,
                    quality_when_it_works = 4,
                    wave_consistency = 4,
                    dificult = 4,
                    windsurf_y_kitesurf = 2,
                    people_to_Water = 3,
                    surf_fore_cast_link = '<link href="//www.surf-forecast.com/stylesheets/widget.css" media="screen" rel="stylesheet" type="text/css" /><div class="wf-width-cont surf-fc-widget"><div class="widget-container"><div class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" src="//www.surf-forecast.com/breaks/Cabo-Roche/forecasts/widget/a" scrolling="no" frameborder="0" marginwidth="0" marginheight="0"></iframe></div></div></div>'
                ),
                Beach(
                    name = "Barbate",
                    image = "/statics/beaches/barbate_river/barbate_river_1.jpg",
                    description = "Barbate River in Andalucia is an exposed river break "
                    +"that does not work very often. Winter and spring are the best times "
                    +"of year to visit. Offshore winds blow from the northeast. Windswells "
                    +"and groundswells in equal measure and the best swell direction is from "
                    +"the southwest. The river breaks consists of lefts. When it's working here, "
                    +"it can get crowded.",
                    type = "River",
                    flag = 3,
                    quality_when_it_works = 5,
                    wave_consistency = 3,
                    difficulty = 3,
                    windsurf_y_kitesurf = 1,
                    people_to_Water = 3,
                    sea_weends = 2,
                    other_options = 4,
                    water_quality = 5,
                    access = 5,
                    scenery = 5,
                    local_attitude = 2,
                    accommodation = 5,
                    camping = 2,
                    entertainment = 5,
                    equipment_and_repairs = 3,
                    restaurants = 5,
                    pubs = 5,
                    surf_fore_cast_link = '<link href="//www.surf-forecast.com/stylesheets/widget.css" media="screen" rel="stylesheet" type="text/css" /><div class="wf-width-cont surf-fc-widget"><div class="widget-container"><div class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" src="//www.surf-forecast.com/breaks/Barbate-River/forecasts/widget/a" scrolling="no" frameborder="0" marginwidth="0" marginheight="0"></iframe></div</div></div>'
                ),
                Beach(
                    name = "Bolonia",
                    image = "/statics/beaches/bolonia/bolonia_1.jpg",
                    description = "Bolonia in Andalucia is a fairly exposed beach break that has fairly consistent surf, although "
                    +"summer tends to be mostly flat. Works best in offshore winds from the northeast. Windswells and groundswells "
                    +"in equal measure and the ideal swell direction is from the southwest. Waves at the beach break both left and "
                    +"right. Rarely crowded here.",
                    type = "Beach",
                    flag = 3,
                    quality_when_it_works = 2,
                    wave_consistency = 3,
                    difficulty = 1,
                    windsurf_y_kitesurf = 2,
                    people_to_Water = 4,
                    surf_fore_cast_link = '<link href="//www.surf-forecast.com/stylesheets/widget.css" media="screen" rel="stylesheet" type="text/css" /><div class="wf-width-cont surf-fc-widget"><div class="widget-container"><div class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" src="//www.surf-forecast.com/breaks/Barbate-River/forecasts/widget/a" scrolling="no" frameborder="0" marginwidth="0" marginheight="0"></iframe></div></div></div>'
                ),
                Beach(
                    name = "Zahara de los atunes",
                    image = "/statics/beaches/zahara_de_los_atunes/zahara_de_los_atunes_1.jpg",
                    description = "Zahara de los Atunes in Andalucia is an exposed beach break that "
                    +"has unreliable waves. Winter and spring are the optimum times of year to visit. "
                    +"Offshore winds are from the northeast. Waves just as likely from local windswells "
                    +"as from distant groundswells and the ideal swell angle is from the southwest. "
                    +"Waves at the beach break both left and right. Good surf at all stages of the tide. "
                    +"Rarely crowded here.",
                    type = "Beach",
                    flag = 2,
                    quality_when_it_works = 4,
                    wave_consistency = 3,
                    difficulty = 2,
                    windsurf_y_kitesurf = 5,
                    people_to_Water = 5,
                    surf_fore_cast_link = '<link href="//www.surf-forecast.com/stylesheets/widget.css" media="screen" rel="stylesheet" type="text/css" /><div class="wf-width-cont surf-fc-widget"><div class="widget-container"><div class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" src="//www.surf-forecast.com/breaks/Zaharadelos-Atunes/forecasts/widget/a" scrolling="no" frameborder="0" marginwidth="0" marginheight="0"></iframe></div></div></div>'
                ),
                Beach(
                    name = "Canos de meca",
                    image = "statics/beaches/canos_de_meca/canos_de_meca_1.jpg",
                    description = "Canos de Meca in Andalucia is an exposed reef break that has quite "
                    +"reliable surf. Winter and spring are the best times of year to visit. The best "
                    +"wind direction is from the northeast with some shelter here from west winds. Poor "
                    +"surf in light onshore winds Most of the surf here comes from groundswells and the "
                    +"optimum swell angle is from the southwest. Right and better left hand reef breaks.. "
                    +"Best around low tide. Often Crowded. Rocks are a hazard.",
                    type= "Reef",
                    flag = 3,
                    quality_when_it_works = 5,
                    wave_consistency = 3,
                    difficulty = 4,
                    windsurf_y_kitesurf = 4,
                    people_to_Water = 2,
                    surf_fore_cast_link = '<link href="//www.surf-forecast.com/stylesheets/widget.css" media="screen" rel="stylesheet" type="text/css" /><div class="wf-width-cont surf-fc-widget"><div class="widget-container"><div class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" src="//www.surf-forecast.com/breaks/Canosde-Meca/forecasts/widget/a" scrolling="no" frameborder="0" marginwidth="0" marginheight="0"></iframe></div></div></div>'
                ),
                Beach(
                    name = "Faro de trafalgar",
                    image = "statics/beaches/faro_de_trafalgar/faro_de_trafalgar_1.jpg",
                    description = 'Faro de Trafalgar in Andalucia is an exposed beach break that has quite'
                    +'reliable surf, although summer tends to be mostly flat. The best wind direction is '
                    +'from the east northeast and there is no shelter here from cross shore breezes. Most '
                    +'of the surf comes fis in the form of windswells and the ideal wave angle is from the '
                    +'west southwest. Waves at the beach break both left and right. Surfable at all stages of '
                    +'the tide. It very rarely gets crowded here.',
                    type = "Beach",
                    flag = 2,
                    quality_when_it_works = 3,
                    wave_consistency = 3,
                    difficulty = 4,
                    windsurf_y_kitesurf = 2,
                    people_to_Water = 3,
                    surf_fore_cast_link  = '<link href="//www.surf-forecast.com/stylesheets/widget.css" media="screen" rel="stylesheet" type="text/css" /><div class="wf-width-cont surf-fc-widget"><div class="widget-container"><div class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" src="//www.surf-forecast.com/breaks/Faro-de-Trafalgar/forecasts/widget/a" scrolling="no" frameborder="0" marginwidth="0" marginheight="0"></iframe></div></div></div>'
                ),
                Beach(
                    name = "El Palmar",
                    image = "statics/beaches/el_palmar/el_palmar_1.jpg",
                    description = "Playa El Palmar in Andalucia is a fairly exposed beach break that has reasonably "
                    +"consistent surf. Winter and spring are the best times of year to visit. Works best in offshore "
                    +"winds from the east. Poor surf in light onshore winds Tends to receive a mix of groundswells and "
                    +"windswells and the ideal swell direction is from the southwest. The beach break offers mainly "
                    +"right hand waves. Good surf at all stages of the tide. Often Crowded. Watch out for dangerous rips.",
                    type = "Sandbar",
                    flag = 3,
                    quality_when_it_works = 4,
                    wave_consistency = 4,
                    difficulty = 4,
                    windsurf_y_kitesurf = 2,
                    people_to_Water = 4,
                    local_attitude = 1,
                    surf_fore_cast_link = '<link href="//www.surf-forecast.com/stylesheets/widget.css" media="screen" rel="stylesheet" type="text/css" /><div class="wf-width-cont surf-fc-widget"><div class="widget-container"><div class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" src="//www.surf-forecast.com/breaks/Playa-El-Palmar/forecasts/widget/a" scrolling="no" frameborder="0" marginwidth="0" marginheight="0"></iframe></div></div></div>'
                ),
                Beach(
                    name = "Conil de la frontera",
                    image = "statics/beaches/conil_de_la_frontera/conil_de_la_frontera_1.jpg",
                    description = "Conil de la Frontera in Andalucia is a quite exposed beach "
                    +"break that has inconsistent surf. Summer in particular tends to be flat. "
                    +"Offshore winds are from the east. Groundswells and windswells are equally "
                    +"likely and the best swell direction is from the southwest. The beach breaks "
                    +"peel to the right. Rarely crowded here. Take care of rocks in the line up.",
                    type="Beach",
                    flag = 3,
                    quality_when_it_works = 2,
                    wave_consistency = 2,
                    difficulty = 2,
                    windsurf_y_kitesurf = 3,
                    people_to_Water = 2,
                    sea_weends = 2,
                    other_options = 2,
                    water_quality = 2,
                    access = 3,
                    scenery = 3,
                    local_attitude = 2,
                    accommodation = 3,
                    camping = 1,
                    entertainment = 2,
                    equipment_and_repairs = 2,
                    restaurants = 3,
                    pubs = 2,
                    surf_fore_cast_link = '<link href="//www.surf-forecast.com/stylesheets/widget.css" media="screen" rel="stylesheet" type="text/css" /><div class="wf-width-cont surf-fc-widget"><div class="widget-container"><div class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" src="//www.surf-forecast.com/breaks/Conildela-Frontera/forecasts/widget/a" scrolling="no" frameborder="0" marginwidth="0" marginheight="0"></iframe></div></div></div>'
                ),
                Beach(
                    name = "El balneario",
                    image = "statics/beaches/el_balneario/el_balneario_1.jpg",
                    description = "El Balneario in Andalucia is an exposed beach break "
                    +"that has fairly consistent surf, although summer tends to be mostly flat. "
                    +"The best wind direction is from the east northeast. Tends to receive a mix "
                    +"of groundswells and windswells and the ideal swell angle is from the west southwest. "
                    +"The beach break offers both left and right hand waves. Surfable at all stages of the tide. "
                    +"It's sometimes crowded here. Crowds may reach hazard levels at this break - consider "
                    +"wearing a lid.",
                    type = "Beach",
                    flag = 3,
                    quality_when_it_works = 4,
                    wave_consistency = 3,
                    difficulty = 2,
                    windsurf_y_kitesurf = 3,
                    people_to_Water = 3,
                    surf_fore_cast_link = '<link href="//www.surf-forecast.com/stylesheets/widget.css" media="screen" rel="stylesheet" type="text/css" /><div class="wf-width-cont surf-fc-widget"><div class="widget-container"><div class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" src="//www.surf-forecast.com/breaks/El-Balneario/forecasts/widget/a" scrolling="no" frameborder="0" marginwidth="0" marginheight="0"></iframe></div></div></div>'
                ),
                Beach(
                    name = "Los lances",
                    image = "statics/beaches/los_lances/los_lances_1.jpg",
                    description = "Los Lances in Andalucia is an exposed beach break that does not work "
                    +"very often. Winter and spring are the optimum times of year to visit. The best wind "
                    +"direction is from the northeast. Windswells and groundswells in equal measure and the "
                    +"ideal swell direction is from the southwest. Waves at the beach break both left and right. "
                    +"Good surf at all stages of the tide. Rarely crowded here. Take care of the strong rips here.",
                    type = "Beach",
                    flag = 1,
                    quality_when_it_works = 3,
                    wave_consistency = 2,
                    difficulty = 3,
                    windsurf_y_kitesurf = 5,
                    people_to_Water = 3,
                    sea_weends = 3,
                    other_options = 3,
                    water_quality = 4,
                    access = 5,
                    scenery = 5,
                    local_attitude = 5,
                    accommodation = 5,
                    camping = 3,
                    entertainment = 3,
                    equipment_and_repairs = 5,
                    restaurants = 5,
                    pubs = 5,
                    surf_fore_cast_link = '<link href="//www.surf-forecast.com/stylesheets/widget.css" media="screen" rel="stylesheet" type="text/css" /><div class="wf-width-cont surf-fc-widget"><div class="widget-container"><div class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" src="//www.surf-forecast.com/breaks/Los-Lances/forecasts/widget/a" scrolling="no" frameborder="0" marginwidth="0" marginheight="0"></iframe></div></div></div>'
                ),
                Beach(
                    name = "Getares",
                    iamge = "statics/beaches/getares/getares_1.jpg",
                    description = "Getares in Andalucia is an exposed beach and reef break that has "
                    +"unreliable waves. Summer offers the optimum conditions for surfing. Works best in "
                    +"offshore winds from the west. There is too little fetch for groundswells to form and "
                    +"the ideal wave direction is from the east. Waves at the beach are both lefts and rights. "
                    +"Good surf at all stages of the tide. Rarely crowded here. Dangerous rips are a hazard of "
                    +"surfing here.",
                    type = "Beach and reef",
                    flag = 3,
                    quality_when_it_works = 3,
                    wave_consistency = 2,
                    difficulty = 1,
                    windsurf_y_kitesurf = 2,
                    people_to_Water = 3,
                    sea_weends = 3,
                    other_options = 2,
                    water_quality = 2,
                    access = 5,
                    scenery = 2,
                    local_attitude = 5,
                    accommodation = 3,
                    camping = 1,
                    entertainment = 3,
                    equipment_and_repairs = 2,
                    restaurants = 5,
                    pubs = 4,
                    surf_fore_cast_link = '<link href="//www.surf-forecast.com/stylesheets/widget.css" media="screen" rel="stylesheet" type="text/css" /><div class="wf-width-cont surf-fc-widget"><div class="widget-container"><div class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" src="//www.surf-forecast.com/breaks/Getares/forecasts/widget/a" scrolling="no" frameborder="0" marginwidth="0" marginheight="0"></iframe></div></div></div>'
                ),
                Beach(
                    
                )













                
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

                
