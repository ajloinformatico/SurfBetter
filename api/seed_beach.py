from models import Beach, DescriptionPoints
from extensions import db


def seed_description_points(app):
    with app.app_context():
        if db.session.query(DescriptionPoints).count() < 1:
            db.session.add_all(
                [
                    DescriptionPoints(
                        name="Quality when ir works",
                        point_info="(1: Even with a perfect swell and wind, the waves are not good. 5: With good "
                                   "conditions, the waves will be world class). "
                    ),
                    DescriptionPoints(
                        name="Wave consistency",
                        point_info="(1: It is a fickle surf spot that only works a few times a year. 5: "
                                   "Reliable "
                                   "year-round spot). "
                    ),
                    DescriptionPoints(
                        name="Difficulty",
                        point_info="(1: Good for beginners. 3: Intermediate. 5: Expert Surfers only)."
                    ),
                    DescriptionPoints(
                        name="Windsurf y kitesurf",
                        point_info="(1: An unsuitable location. 5: The wind and swell at the beach are often "
                                   "excellent). "
                    ),
                    DescriptionPoints(
                        name="People to water",
                        point_info="(1: There are many people frequently. 5: the beach is an easy place for our "
                                   "surfers). "
                    ),
                    DescriptionPoints(
                        name="Sea Weends",
                        point_info="(1: Even a light sea wind ruins the water plane. 5: The beach can offer "
                                   "better waves with a little sea wind). "
                    ),
                    DescriptionPoints(
                        name="Other options",
                        point_info="(1: If wind or tidal conditions are not good for the beach, they will also "
                                   "not be good for other nearby spots. 5: Other nearby spots offer a rich variety of "
                                   "wind and "
                                   "wave exposures) "
                    ),
                    DescriptionPoints(
                        name="Water Quality",
                        point_info="1: Health risks due to contamination. 5: There is never pollution)."
                    ),
                    DescriptionPoints(
                        name="Access",
                        point_info="(1: Requires an overland expedition or boat rental. 3: A 30-minute walk from the "
                                   "nearest parking lot. 5: Parking in front of the Spot). "
                    ),
                    DescriptionPoints(
                        name="Scenery",
                        point_info="(1: A horrible industrial landscape. 5: A spectacular natural landscape)."
                    ),
                    DescriptionPoints(
                        name="Local attitude",
                        point_info="(1: Local surfers don't like visitors. 5: There are no local surfers, or if there "
                                   "are, they are hospitable and friendly). "
                    ),
                    DescriptionPoints(
                        name="Accommodation",
                        point_info="(1: No accommodation. 5: Many accommodation options near the beach for all "
                                   "budgets "
                                   "from hostels to luxury hotels). "
                    ),
                    DescriptionPoints(
                        name="Camping",
                        point_info="(1: It is not possible to camp at the beach. 3: It is possible to camp, but there "
                                   "are no facilities. 5: A nearby campsite that has excellent facilities and good "
                                   "vibes). "
                    ),
                    DescriptionPoints(
                        name="Entertainment",
                        point_info="(1: Besides surfing and solitude there is nothing to do when there are no waves. "
                                   "5: The beach is in such an interesting area, surfing there is a bonus). "
                    ),
                    DescriptionPoints(
                        name="Equipment and repairs",
                        point_info="(1: You can't buy anything, not even wax. 5: Quality surf gear for purchase or "
                                   "rental with repairs available). "
                    ),
                    DescriptionPoints(
                        name="Restaurants",
                        point_info="(1: Bring your own food, there isn't even a store. 5: Many different "
                                   "restaurants and bars in the beach, from fast food to fancy restaurants)."
                    ),
                    DescriptionPoints(
                        name="Pubs",
                        point_info="(1: Alcohol is prohibited in the country. 5: There is an excellent bar, near the "
                                   "beach where you can park the van for the night). "
                    )
                ]
            )
            db.session.commit()


def seed_beaches(app):
    # Beaches seeder
    with app.app_context():
        if db.session.query(Beach).count() < 1:
            db.session.add_all(
                [
                    Beach(
                        id=1,
                        name="La Muralla",
                        image="/statics/beaches/la_muralla/playa_de_la_muralla_1.jpg",
                        description="La Muralla in Andalucia is a quite exposed reef break "
                                    + "that has fairly consistent surf. Winter and spring are the optimum "
                                    + "times of year to visit. Offshore winds are from the north. Tends to "
                                    + "receive a mix of groundswells and windswells and the best swell direction "
                                    + "is from the southwest. A right hand reef. Best around mid tide when the tide "
                                    + "is rising. It's often crowded here. Watch out for rocks.",
                        type_beach="Reef",
                        flag=3,
                        quality_when_it_works=3,
                        wave_consistency=3,
                        difficulty=2,
                        windsurf_y_kitesurf=1,
                        people_to_water=4,
                        sea_weends=3,
                        other_options=2,
                        water_quality=3,
                        access=5,
                        scenery=3,
                        local_attitude=5,
                        accommodation=5,
                        camping=3,
                        entertainment=5,
                        equipment_and_repairs=2,
                        restaurants=5,
                        pubs=5,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div '
                                            'class="widget-container"><div class="external-cont"><iframe '
                                            'class="surf-fc-i" '
                                            'allowtransparency="true" src="//www.surf-forecast.com/breaks/La-Muralla'
                                            '/forecasts/widget/a" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        longitude=36.58007651382025,
                        latitude=-6.265659586583074
                    ),
                    Beach(
                        id=2,
                        name="Las Redes",
                        image="/statics/beaches/las_redes/las_redes_1.jpg",
                        description="Las Redes in Andalucia is a reasonably exposed beach "
                                    + "break that has pretty consitent surf. Winter and spring are the best "
                                    + "times of year to visit. Offshore winds are from the north northeast. "
                                    + "Tends to receive a mix of groundswells and windswells and the ideal swell "
                                    + "direction is from the west southwest. Waves at the beach are both lefts and "
                                    + "rights. Best around mid tide when the tide is rising. When the surf is up, it "
                                    + "can get quite busy in the water. It can even get crowded enough to be "
                                    + "dangerous.",
                        type_beach="Sandbar",
                        flag=3,
                        quality_when_it_works=3,
                        wave_consistency=2,
                        difficulty=3,
                        windsurf_y_kitesurf=4,
                        people_to_water=3,
                        sea_weends=4,
                        other_options=4,
                        water_quality=3,
                        access=5,
                        scenery=2,
                        local_attitude=3,
                        accommodation=5,
                        camping=3,
                        entertainment=5,
                        equipment_and_repairs=5,
                        restaurants=4,
                        pubs=5,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div '
                                            'class="widget-container"><div class="external-cont"><iframe '
                                            'class="surf-fc-i" '
                                            'allowtransparency="true" src="//www.surf-forecast.com/breaks/Las-Redes'
                                            '/forecasts/widget/a" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        longitude=36.60087430725243,
                        latitude=-6.27760624484712
                    ),
                    Beach(
                        id=3,
                        name="La Playita",
                        image="/statics/beaches/la_playita/la_playita_1.jpg",
                        description="La Playita in Andalucia is an exposed beach break that has reasonably consistent "
                                    "surf. "
                                    + "Winter and spring are the optimum times of year to visit. Ideal winds are from "
                                      "the "
                                      "northeast. Tends "
                                    + "to receive a mix of groundswells and windswells and the best swell direction is "
                                      "from the southwest. "
                                    + "Waves at the beach break both left and right. A popular wave that can get "
                                      "growded. "
                                      "Watch out for rocks.",
                        type_beach="Beach",
                        flag=1,
                        quality_when_it_works=3,
                        wave_consistency=3,
                        difficulty=3,
                        windsurf_y_kitesurf=1,
                        people_to_water=2,
                        sea_weends=4,
                        other_options=4,
                        water_quality=3,
                        access=5,
                        scenery=3,
                        local_attitude=5,
                        accommodation=3,
                        camping=3,
                        entertainment=4,
                        equipment_and_repairs=4,
                        restaurants=3,
                        pubs=3,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div '
                                            'class="widget-container"><div class="external-cont"><iframe '
                                            'class="surf-fc-i" '
                                            'allowtransparency="true" src="//www.surf-forecast.com/breaks/Las-Caracolas'
                                            '/forecasts/widget/a" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        longitude=36.817668803925,
                        latitude=-5.375303773894092
                    ),
                    Beach(
                        id=4,
                        name="Las Caracolas",
                        image="/statics/beaches/las_caracolas/las_caracolas_1.jpg",
                        description="Las Caracolas in Andalucia is an exposed beach "
                                    + "and reef break that has fairly consistent surf. Winter and spring "
                                    + "are the best times of year to visit. The best wind direction is "
                                    + "from the northeast. Most of the surf here comes from groundswells "
                                    + "and the ideal swell direction is from the southwest. Waves at the beach "
                                    + "break both left and right. Best around mid tide. Likely to be crowded if "
                                      "working. "
                                      "Watch out for rocks. ",
                        type_beach="Beach and reef",
                        flag=2,
                        quality_when_it_works=3,
                        wave_consistency=3,
                        difficulty=2,
                        windsurf_y_kitesurf=5,
                        people_to_water=3,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div '
                                            'class="widget-container"><div class="external-cont"><iframe '
                                            'class="surf-fc-i" '
                                            'allowtransparency="true" src="//www.surf-forecast.com/breaks/Las'
                                            '-Caracolas/forecasts/widget/a" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe><div class="footer"><a '
                                            'class="logo" href="//www.surf-forecast.com/"><img '
                                            'src="//www.surf-forecast.com/images/widget.png" alt="Widget" width="1" '
                                            'height="1" /></a><div '
                                            'class="about" id="cmt">More <a '
                                            'href="//www.surf-forecast.com/breaks/Las-Caracolas">Detailed Surf '
                                            'Conditions &amp; Webcams for&nbsp;Las Caracolas</a> <nobr>at&nbsp;<a '
                                            'href="//www.surf-forecast.com/">surf-forecast.com</a></nobr>.</div></div'
                                            '></div></div></div>',
                        latitude=37.191849213692905,
                        longitude=-1.8146496019467826
                    ),
                    Beach(
                        id=5,
                        name="la Cabanita",
                        image="/statics/beaches/la_cabanita/la_cabanita_1.jpg",
                        description="La Cabanita in Andalucia is an exposed reef "
                                    + "break that only works when conditions are just right. Winter "
                                    + "and spring are the best times of year to visit. Offshore winds "
                                    + "are from the north northeast. Windswells and groundswells in equal "
                                    + "measure and the ideal swell direction is from the west southwest. "
                                    + "A right hand reef break. Good surf at all stages of the tide. Rarely "
                                    + "crowded here. Submerged rocks are a hazard.",
                        type_beach="Beach",
                        flag=2,
                        quality_when_it_works=3,
                        wave_consistency=2,
                        difficulty=3,
                        windsurf_y_kitesurf=2,
                        people_to_water=3,
                        sea_weends=3,
                        other_options=3,
                        water_quality=3,
                        access=5,
                        scenery=2,
                        local_attitude=2,
                        accommodation=4,
                        camping=4,
                        entertainment=4,
                        equipment_and_repairs=3,
                        restaurants=4,
                        pubs=3,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div '
                                            'class="widget-container"><div class="external-cont"><iframe '
                                            'class="surf-fc-i" '
                                            'allowtransparency="true" src="//www.surf-forecast.com/breaks/La-Cabanita'
                                            '/forecasts/widget/a" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=36.50593527086339,
                        longitude=-4.910418991198296
                    ),
                    Beach(
                        id=6,
                        name="Torre Gorda",
                        image="/statics/beaches/torre_gorda/torre_gorda_1.jpg",
                        description="Torre Gorda in Andalucia is an exposed beach break that does not work very often. "
                                    + "Winter and spring are the best times of year to visit. The best wind direction "
                                      "is "
                                      "from the "
                                    + "east northeast. Tends to receive a mix of groundswells and windswells and the "
                                      "ideal swell "
                                    + "direction is from the west. The beach breaks offer lefts and rights. Best "
                                      "around "
                                      "high tide. "
                                    + "Rarely crowded here.",
                        type_beach="Beach",
                        flag=3,
                        quality_when_it_works=1,
                        wave_consistency=2,
                        difficulty=4,
                        windsurf_y_kitesurf=3,
                        people_to_water=4,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div '
                                            'class="widget-container"><div class="external-cont"><iframe '
                                            'class="surf-fc-i" '
                                            'allowtransparency="true" src="//www.surf-forecast.com/breaks/Torre-Gorda'
                                            '/forecasts/widget/a" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=36.45654187290273,
                        longitude=-6.251923015154041
                    ),
                    Beach(
                        id=7,
                        name="Playa de Camposoto",
                        image="/statics/beaches/playa_de_camposoto/playa_de_camposoto_1.jpg",
                        description="Playa Campo Sota in Andalucia is an exposed beach break that "
                                    + "has quite reliable surf. Winter and spring are the optimum times of year to "
                                      "visit. "
                                    + "Ideal winds are from the east northeast. Windswells and groundswells in equal "
                                      "measure "
                                    + "and the optimum swell angle is from the west southwest. The beach breaks offer "
                                      "lefts and "
                                    + "rights. It's often crowded here.",
                        type_beach="Beach",
                        flag=3,
                        quality_when_it_works=3,
                        wave_consistency=3,
                        difficulty=3,
                        windsurf_y_kitesurf=2,
                        people_to_water=3,
                        sea_weends=3,
                        other_options=3,
                        water_quality=5,
                        access=5,
                        scenery=4,
                        local_attitude=2,
                        accommodation=2,
                        camping=1,
                        entertainment=3,
                        equipment_and_repairs=2,
                        restaurants=3,
                        pubs=2,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div '
                                            'class="widget-container"><div class="external-cont"><iframe '
                                            'class="surf-fc-i" '
                                            'allowtransparency="true" src="//www.surf-forecast.com/breaks/Playa-Campo'
                                            '-Sota/forecasts/widget/a '
                                            '" scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=36.426356570332956,
                        longitude=-6.229675819031719
                    ),
                    Beach(
                        id=8,
                        name="Chiclana de la frontera",
                        image="/statics/beaches/chiclana_de_frontera/chiclana_de_la_frontera_1.jpg",
                        description="Chiclana de la Frontera in Andalucia is an "
                                    + "exposed beach break that has inconsistent surf. Summer in "
                                    + "particular tends to be flat. The best wind direction is from "
                                    + "the east. Waves just as likely from local windswells as from "
                                    + "distant groundswells and the ideal swell direction is from the "
                                    + "southwest. The beach break provides left and right handers.",
                        type_beach="Beach",
                        flag=3,
                        quality_when_it_works=2,
                        wave_consistency=2,
                        difficulty=3,
                        windsurf_y_kitesurf=1,
                        people_to_water=3,
                        water_quality=3,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div '
                                            'class="widget-container"><div class="external-cont"><iframe '
                                            'class="surf-fc-i" '
                                            'allowtransparency="true" '
                                            'src="//www.surf-forecast.com/breaks/Chiclanadela-Frontera/forecasts'
                                            '/widget/a '
                                            '" scrolling="no" '
                                            'frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=36.3364347559575,
                        longitude=-6.163902414699233
                    ),
                    Beach(
                        id=9,
                        name="El Castillo",
                        image="/statics/beaches/el_castillo/el_castillo_1.jpg",
                        description="El Castillo in Andalucia is an exposed point break that has inconsistent "
                                    + "surf. Winter is the best time of year for surfing here. Ideal winds are from "
                                      "the "
                                      "east "
                                    + "southeast and there is no shelter here from cross shore breezes. Tends to "
                                      "receive "
                                      "a mix "
                                    + "of groundswells and windswells and the best swell direction is from the west "
                                      "southwest. "
                                    + "No point break here. Best around mid tide. Rarely crowded here. Rocks are a "
                                      "hazard.",
                        type_beach="Point",
                        flag=2,
                        quality_when_it_works=4,
                        wave_consistency=3,
                        difficulty=4,
                        windsurf_y_kitesurf=1,
                        people_to_water=3,
                        sea_weends=1,
                        other_options=5,
                        water_quality=5,
                        access=3,
                        scenery=4,
                        local_attitude=4,
                        accommodation=4,
                        camping=3,
                        entertainment=3,
                        equipment_and_repairs=2,
                        restaurants=4,
                        pubs=1,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div '
                                            'class="widget-container"><div class="external-cont"><iframe '
                                            'class="surf-fc-i" '
                                            'allowtransparency="true" src="//www.surf-forecast.com/breaks/El-Castillo'
                                            '/forecasts/widget/a" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=36.372473575190526,
                        longitude=-6.18680955163413
                    ),
                    Beach(
                        id=10,
                        name="La Barrosa",
                        image="/statics/beaches/la_barrosa/la_barrosa_1.jpg",
                        description="La Barossa in Andalucia is an exposed beach "
                                    + "break that has reasonably consistent surf, although summer "
                                    + "tends to be mostly flat. Offshore winds are from the east "
                                    + "northeast and there is no shelter here from cross shore breezes. "
                                    + "Most of the surf here comes from groundswells and the best swell "
                                    + "direction is from the west southwest. The beach break provides left "
                                    + "and right handers. Good surf at all stages of the tide. Rarely crowded here. "
                                    + "Beware of buoys, fishing nets,pollution.",
                        type_beach="Beach",
                        flag=3,
                        quality_when_it_works=3,
                        wave_consistency=3,
                        difficulty=2,
                        windsurf_y_kitesurf=3,
                        people_to_water=4,
                        sea_weends=2,
                        other_options=2,
                        water_quality=4,
                        access=5,
                        scenery=5,
                        local_attitude=4,
                        accommodation=5,
                        camping=1,
                        entertainment=5,
                        equipment_and_repairs=1,
                        restaurants=5,
                        pubs=5,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div '
                                            'class="widget-container"><div class="external-cont"><iframe '
                                            'class="surf-fc-i" '
                                            'allowtransparency="true" src="//www.surf-forecast.com/breaks/La-Barossa'
                                            '/forecasts/widget/a" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=36.3441416209236,
                        longitude=-6.1667648648905855
                    ),
                    Beach(
                        id=11,
                        name="Cabo Roche",
                        image="/statics/beaches/cabo_roche/cabo_roche_1.jpg",
                        description="Cabo Roche in Andalucia is an exposed beach break that has dependable "
                                    + "surf. Winter and spring are the optimum times of year to visit. The best wind "
                                      "direction "
                                    + "is from the east. Tends to receive a mix of groundswells and windswells and the "
                                      "best swell "
                                    + "direction is from the southwest. Waves at the beach break both left and right. "
                                      "It's sometimes "
                                    + "crowded here. Watch out for rocks.",
                        type_beach="Beach",
                        flag=2,
                        quality_when_it_works=4,
                        wave_consistency=4,
                        difficulty=4,
                        windsurf_y_kitesurf=2,
                        people_to_water=3,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div '
                                            'class="widget-container"><div class="external-cont"><iframe '
                                            'class="surf-fc-i" '
                                            'allowtransparency="true" src="//www.surf-forecast.com/breaks/Cabo-Roche'
                                            '/forecasts/widget/a" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=36.29386174696467,
                        longitude=-6.137035829557673
                    ),
                    Beach(
                        id=12,
                        name="Barbate",
                        image="/statics/beaches/barbate_river/barbate_river_1.jpg",
                        description="Barbate River in Andalucia is an exposed river break "
                                    + "that does not work very often. Winter and spring are the best times "
                                    + "of year to visit. Offshore winds blow from the northeast. Windswells "
                                    + "and groundswells in equal measure and the best swell direction is from "
                                    + "the southwest. The river breaks consists of lefts. When it's working here, "
                                    + "it can get crowded.",
                        type_beach="River",
                        flag=3,
                        quality_when_it_works=5,
                        wave_consistency=3,
                        difficulty=3,
                        windsurf_y_kitesurf=1,
                        people_to_water=3,
                        sea_weends=2,
                        other_options=4,
                        water_quality=5,
                        access=5,
                        scenery=5,
                        local_attitude=2,
                        accommodation=5,
                        camping=2,
                        entertainment=5,
                        equipment_and_repairs=3,
                        restaurants=5,
                        pubs=5,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div '
                                            'class="widget-container"><div class="external-cont"><iframe '
                                            'class="surf-fc-i" '
                                            'transparency="true" src="//www.surf-forecast.com/breaks/Barbate-River'
                                            '/forecasts/widget/a" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div</div></div>',
                        latitude=36.1860400852292,
                        longitude=-5.918425296832528
                    ),
                    Beach(
                        id=13,
                        name="Bolonia",
                        image="/statics/beaches/bolonia/bolonia_1.jpg",
                        description="Bolonia in Andalucia is a fairly exposed beach break that has fairly consistent "
                                    "surf, although "
                                    + "summer tends to be mostly flat. Works best in offshore winds from the "
                                      "northeast. "
                                      "Windswells and groundswells "
                                    + "in equal measure and the ideal swell direction is from the southwest. Waves at "
                                      "the "
                                      "beach break both left and "
                                    + "right. Rarely crowded here.",
                        type_beach="Beach",
                        flag=3,
                        quality_when_it_works=2,
                        wave_consistency=3,
                        difficulty=1,
                        windsurf_y_kitesurf=2,
                        people_to_water=4,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div '
                                            'class="widget-container"><div class="external-cont"><iframe '
                                            'class="surf-fc-i" '
                                            'allowtransparency="true" src="//www.surf-forecast.com/breaks/Barbate-River'
                                            '/forecasts/widget/a" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=36.08790770253498,
                        longitude=-5.774991450446252

                    ),
                    Beach(
                        id=14,
                        name="Zahara de los atunes",
                        image="/statics/beaches/zahara_de_los_atunes/zahara_de_los_atunes_1.jpg",
                        description="Zahara de los Atunes in Andalucia is an exposed beach break that "
                                    + "has unreliable waves. Winter and spring are the optimum times of year to visit. "
                                    + "Offshore winds are from the northeast. Waves just as likely from local "
                                      "windswells "
                                    + "as from distant groundswells and the ideal swell angle is from the southwest. "
                                    + "Waves at the beach break both left and right. Good surf at all stages of the "
                                      "tide. "
                                    + "Rarely crowded here.",
                        type_beach="Beach",
                        flag=2,
                        quality_when_it_works=4,
                        wave_consistency=3,
                        difficulty=2,
                        windsurf_y_kitesurf=5,
                        people_to_water=5,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div '
                                            'class="widget-container"><div class="external-cont"><iframe '
                                            'class="surf-fc-i" '
                                            'allowtransparency="true" src="//www.surf-forecast.com/breaks/Zaharadelos'
                                            '-Atunes/forecasts/widget '
                                            '/a" scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=36.15450537923463,
                        longitude=-5.870086550235356
                    ),
                    Beach(
                        id=15,
                        name="Caños de meca",
                        image="/statics/beaches/canos_de_meca/canos_de_meca_1.jpg",
                        description="Canos de Meca in Andalucia is an exposed reef break that has quite "
                                    + "reliable surf. Winter and spring are the best times of year to visit. The best "
                                    + "wind direction is from the northeast with some shelter here from west winds. "
                                      "Poor "
                                    + "surf in light onshore winds Most of the surf here comes from groundswells and "
                                      "the "
                                    + "optimum swell angle is from the southwest. Right and better left hand reef "
                                      "breaks.. "
                                    + "Best around low tide. Often Crowded. Rocks are a hazard.",
                        type_beach="Reef",
                        flag=3,
                        quality_when_it_works=5,
                        wave_consistency=3,
                        difficulty=4,
                        windsurf_y_kitesurf=4,
                        people_to_water=2,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div '
                                            'class="widget-container"><div class="external-cont"><iframe '
                                            'class="surf-fc-i" '
                                            'allowtransparency="true" src="//www.surf-forecast.com/breaks/Canosde'
                                            '-Meca/forecasts/widget/a" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=36.18671205191269,
                        longitude=-6.026231000333102
                    ),
                    Beach(
                        id=16,
                        name="Faro de trafalgar",
                        image="/statics/beaches/faro_de_trafalgar/faro_de_trafalgar_1.jpg",
                        description='Faro de Trafalgar in Andalucia is an exposed beach break that has quite'
                                    + 'reliable surf, although summer tends to be mostly flat. The best wind '
                                      'direction is '
                                    + 'from the east northeast and there is no shelter here from cross shore breezes. '
                                      'Most '
                                    + 'of the surf comes fis in the form of windswells and the ideal wave angle is '
                                      'from '
                                      'the '
                                    + 'west southwest. Waves at the beach break both left and right. Surfable at all '
                                      'stages of '
                                    + 'the tide. It very rarely gets crowded here.',
                        type_beach="Beach",
                        flag=2,
                        quality_when_it_works=3,
                        wave_consistency=3,
                        difficulty=4,
                        windsurf_y_kitesurf=2,
                        people_to_water=3,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div '
                                            'class="widget-container"><div class="external-cont"><iframe '
                                            'class="surf-fc-i" '
                                            'allowtransparency="true" src="//www.surf-forecast.com/breaks/Faro-de'
                                            '-Trafalgar/forecasts/widget '
                                            '/a" scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=36.184740503406545,
                        longitude=-6.036062645294939
                    ),
                    Beach(
                        id=17,
                        name="El Palmar",
                        image="/statics/beaches/el_palmar/el_palmar_1.jpg",
                        description="Playa El Palmar in Andalucia is a fairly exposed beach break that has reasonably "
                                    + "consistent surf. Winter and spring are the best times of year to visit. Works "
                                      "best "
                                      "in offshore "
                                    + "winds from the east. Poor surf in light onshore winds Tends to receive a mix of "
                                      "groundswells and "
                                    + "windswells and the ideal swell direction is from the southwest. The beach break "
                                      "offers mainly "
                                    + "right hand waves. Good surf at all stages of the tide. Often Crowded. Watch out "
                                      "for dangerous rips.",
                        type_beach="Sandbar",
                        flag=3,
                        quality_when_it_works=4,
                        wave_consistency=4,
                        difficulty=4,
                        windsurf_y_kitesurf=2,
                        people_to_water=4,
                        local_attitude=1,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div class="widget-container"><div '
                                            'class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" '
                                            'src="//www.surf-forecast.com/breaks/Playa-El-Palmar/forecasts/widget/a" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=36.24080882886089,
                        longitude=-6.0771007126081535
                    ),
                    Beach(
                        id=18,
                        name="Conil de la frontera",
                        image="/statics/beaches/conil_de_la_frontera/conil_de_la_frontera_1.jpg",
                        description="Conil de la Frontera in Andalucia is a quite exposed beach "
                                    + "break that has inconsistent surf. Summer in particular tends to be flat. "
                                    + "Offshore winds are from the east. Groundswells and windswells are equally "
                                    + "likely and the best swell direction is from the southwest. The beach breaks "
                                    + "peel to the right. Rarely crowded here. Take care of rocks in the line up.",
                        type_beach="Beach",
                        flag=3,
                        quality_when_it_works=2,
                        wave_consistency=2,
                        difficulty=2,
                        windsurf_y_kitesurf=3,
                        people_to_water=2,
                        sea_weends=2,
                        other_options=2,
                        water_quality=2,
                        access=3,
                        scenery=3,
                        local_attitude=2,
                        accommodation=3,
                        camping=1,
                        entertainment=2,
                        equipment_and_repairs=2,
                        restaurants=3,
                        pubs=2,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div class="widget-container"><div '
                                            'class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" '
                                            'src="//www.surf-forecast.com/breaks/Conildela-Frontera/forecasts/widget'
                                            '/a" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=36.28103417470304,
                        longitude=-6.0995557786390595
                    ),
                    Beach(
                        id=19,
                        name="El balneario",
                        image="/statics/beaches/el_balneario/el_balneario_1.jpeg",
                        description="El Balneario in Andalucia is an exposed beach break "
                                    + "that has fairly consistent surf, although summer tends to be mostly flat. "
                                    + "The best wind direction is from the east northeast. Tends to receive a mix "
                                    + "of groundswells and windswells and the ideal swell angle is from the west "
                                      "southwest. "
                                    + "The beach break offers both left and right hand waves. Surfable at all stages "
                                      "of "
                                      "the tide. "
                                    + "It's sometimes crowded here. Crowds may reach hazard levels at this break - "
                                      "consider "
                                    + "wearing a lid.",
                        type_beach="Beach",
                        flag=3,
                        quality_when_it_works=4,
                        wave_consistency=3,
                        difficulty=2,
                        windsurf_y_kitesurf=3,
                        people_to_water=3,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div class="widget-container"><div '
                                            'class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" '
                                            'src="//www.surf-forecast.com/breaks/El-Balneario/forecasts/widget/a" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=36.00990303504987,
                        longitude=-5.605775818641811
                    ),
                    Beach(
                        id=20,
                        name="Los lances",
                        image="/statics/beaches/los_lances/los_lances_1.jpeg",
                        description="Los Lances in Andalucia is an exposed beach break that does not work "
                                    + "very often. Winter and spring are the optimum times of year to visit. The best "
                                      "wind "
                                    + "direction is from the northeast. Windswells and groundswells in equal measure "
                                      "and "
                                      "the "
                                    + "ideal swell direction is from the southwest. Waves at the beach break both left "
                                      "and right. "
                                    + "Good surf at all stages of the tide. Rarely crowded here. Take care of the "
                                      "strong "
                                      "rips here.",
                        type_beach="Beach",
                        flag=1,
                        quality_when_it_works=3,
                        wave_consistency=2,
                        difficulty=3,
                        windsurf_y_kitesurf=5,
                        people_to_water=3,
                        sea_weends=3,
                        other_options=3,
                        water_quality=4,
                        access=5,
                        scenery=5,
                        local_attitude=5,
                        accommodation=5,
                        camping=3,
                        entertainment=3,
                        equipment_and_repairs=5,
                        restaurants=5,
                        pubs=5,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div class="widget-container"><div '
                                            'class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" '
                                            'src="//www.surf-forecast.com/breaks/Los-Lances/forecasts/widget/a" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=36.045447338604276,
                        longitude=-5.6397192448350335
                    ),
                    Beach(
                        id=21,
                        name="Getares",
                        image="/statics/beaches/getares/getares_1.jpg",
                        description="Getares in Andalucia is an exposed beach and reef break that has "
                                    + "unreliable waves. Summer offers the optimum conditions for surfing. Works best "
                                      "in "
                                    + "offshore winds from the west. There is too little fetch for groundswells to "
                                      "form "
                                      "and "
                                    + "the ideal wave direction is from the east. Waves at the beach are both lefts "
                                      "and "
                                      "rights. "
                                    + "Good surf at all stages of the tide. Rarely crowded here. Dangerous rips are a "
                                      "hazard of "
                                    + "surfing here.",
                        type_beach="Beach and reef",
                        flag=3,
                        quality_when_it_works=3,
                        wave_consistency=2,
                        difficulty=1,
                        windsurf_y_kitesurf=2,
                        people_to_water=3,
                        sea_weends=3,
                        other_options=2,
                        water_quality=2,
                        access=5,
                        scenery=2,
                        local_attitude=5,
                        accommodation=3,
                        camping=1,
                        entertainment=3,
                        equipment_and_repairs=2,
                        restaurants=5,
                        pubs=4,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div class="widget-container"><div '
                                            'class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" '
                                            'src="//www.surf-forecast.com/breaks/Getares/forecasts/widget/a" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        longitude=36.096727264019016,
                        latitude=-5.44314921083719
                    ),
                    Beach(
                        id=22,
                        name="El caño de la culata",
                        image="/statics/beaches/el_caño_de_la_culata/el_caño_de_la_culata_1.jpg",
                        description="El Caño de la Culata in Andalucia is a sheltered beach break that has "
                                    + "fairly consistent surf. Winter and spring are the best times of year to visit. "
                                      "Offshore "
                                    + "winds are from the north northeast. Waves just as likely from local windswells "
                                      "as "
                                      "from "
                                    + "distant groundswells and the ideal swell direction is from the south. The beach "
                                      "break "
                                    + "offers both left and right hand waves. When it's working here, it can get "
                                      "crowded. "
                                    + "Take care of the strong rips here.",
                        type_beach="Beach",
                        flag=3,
                        quality_when_it_works=1,
                        wave_consistency=1,
                        difficulty=3,
                        windsurf_y_kitesurf=2,
                        people_to_water=4,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div class="widget-container"><div '
                                            'class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" '
                                            'src="//www.surf-forecast.com/breaks/El-Cano-de-la-Culata/forecasts'
                                            '/widget/a" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=37.227747896715556,
                        longitude=-7.080683179906148
                    ),
                    Beach(
                        id=23,
                        name="El Chanquete",
                        image="/statics/beaches/el_chanquete/el_chanquete_1.jpg",
                        description="El Chanquete in Andalucia is an exposed beach and reef break that "
                                    + "has quite consistent surf, although summer tends to be mostly flat. Offshore "
                                    + "winds blow from the north northeast. Windswells are much more typical than "
                                    + "groudswells and the optimum wave angle is from the southeast. The beach break "
                                    + "offers both left and right hand waves. Good surf at all stages of the tide. "
                                      "When "
                                    + "the surf is up, it can get quite busy in the water. Submerged rocks are a "
                                      "hazard.",
                        type_beach="Beach abd Reef",
                        flag=3,
                        quality_when_it_works=2,
                        wave_consistency=2,
                        difficulty=2,
                        windsurf_y_kitesurf=2,
                        people_to_water=2,
                        sea_weends=5,
                        other_options=2,
                        water_quality=4,
                        access=5,
                        scenery=3,
                        local_attitude=1,
                        accommodation=5,
                        camping=3,
                        entertainment=4,
                        equipment_and_repairs=2,
                        restaurants=5,
                        pubs=5,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div class="widget-container"><div '
                                            'class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" '
                                            'src="//www.surf-forecast.com/breaks/El-Chanquete/forecasts/widget/a" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=36.716624771783444,
                        longitude=-4.348392220767674

                    ),
                    Beach(
                        id=24,
                        name="El Sanset",
                        image="/statics/beaches/el_sanset/el_sanset_1.jpg",
                        description="El Sunset (Benalmádena) in Andalucia "
                                    + "is an exposed beach break that has inconsistent surf. "
                                    + "Autumn and winter are the optimum times of year for waves. "
                                    + "Offshore winds are from the northwest. Windswells are much "
                                    + "more typical than groudswells and the ideal wave direction is "
                                    + "from the southeast. The beach break provides left and right "
                                    + "handers. Good surf at all stages of the tide. A popular wave "
                                    + "that can get growded.",
                        type_beach="Beach",
                        flag=3,
                        quality_when_it_works=4,
                        wave_consistency=4,
                        difficulty=3,
                        windsurf_y_kitesurf=1,
                        people_to_water=2,
                        sea_weends=1,
                        other_options=5,
                        water_quality=5,
                        access=3,
                        scenery=5,
                        local_attitude=1,
                        accommodation=5,
                        camping=1,
                        entertainment=1,
                        equipment_and_repairs=1,
                        restaurants=5,
                        pubs=5,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div class="widget-container"><div '
                                            'class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" '
                                            'src="//www.surf-forecast.com/breaks/El-Sunset-Benalmadena/forecasts'
                                            '/widget/a '
                                            '" scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=36.73481350957522,
                        longitude=-6.441177912387428

                    ),
                    Beach(
                        id=25,
                        name="Fuengirola",
                        image="/statics/beaches/fuengirola/fuengirola_1.jpg",
                        description="Fuengirola in Andalucia is an exposed beach break that has "
                                    + "quite reliable surf, although summer tends to be mostly flat. Offshore "
                                    + "winds blow from the west northwest and there is no shelter here from cross "
                                    + "shore breezes. The location means that groundswells are unknown and the best "
                                    + "wave direction is from the east southeast. The beach break offers both left and "
                                      "right "
                                    + "hand waves. Surfable at all stages of the tide. It's sometimes crowded here. "
                                      "Watch "
                                      "out "
                                    + "for rips and rocks.",
                        type_beach="Beach",
                        flag=2,
                        quality_when_it_works=3,
                        wave_consistency=2,
                        difficulty=3,
                        windsurf_y_kitesurf=4,
                        people_to_water=3,
                        sea_weends=3,
                        other_options=4,
                        water_quality=4,
                        access=5,
                        scenery=4,
                        local_attitude=4,
                        accommodation=5,
                        camping=4,
                        entertainment=5,
                        equipment_and_repairs=5,
                        restaurants=5,
                        pubs=5,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div class="widget-container"><div '
                                            'class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" '
                                            'src="//www.surf-forecast.com/breaks/Fuengirola/forecasts/widget/a" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=36.54421890358208,
                        longitude=-4.617685381429646
                    ),
                    Beach(
                        id=26,
                        name="La Chucha",
                        image="/statics/beaches/la_chucha/la_chucha_1.jpeg",
                        description="La Chucha in Andalucia is a fairly exposed reef break that does not work very "
                                    "often. "
                                    "Summer in particular tends to be flat. The best wind direction is from the north. "
                                    "Windswells are much more typical than groudswells and the best wave direction is "
                                    "from the southeast. There is no reef break. Good surf at all stages of the tide. "
                                    "When the surf is up, it can get quite busy in the water. Beware of rocks, rips.",
                        type_beach="Beach",
                        flag=1,
                        quality_when_it_works=4,
                        wave_consistency=3,
                        difficulty=3,
                        windsurf_y_kitesurf=2,
                        people_to_water=4,
                        sea_weends=5,
                        other_options=1,
                        water_quality=4,
                        access=5,
                        scenery=4,
                        local_attitude=4,
                        camping=2,
                        equipment_and_repairs=2,
                        restaurants=5,
                        pubs=3,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div class="widget-container"><div '
                                            'class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" '
                                            'src="//www.surf-forecast.com/breaks/La-Chucha/forecasts/widget/a" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=36.696499053509584,
                        longitude=-3.4572400332622837
                    ),
                    Beach(
                        id=27,
                        name="La herradura",
                        image="/statics/beaches/la_herradura/la_herradura_1.jpg",
                        description="La Herradura in Andalucia is an exposed beach break that does not work very "
                                    "often. "
                                    "Summer in particular tends to be flat. Offshore winds blow from the northeast. "
                                    "Usually gets local windswells, but groundswells do happen and the best wave "
                                    "direction is from the southwest. Waves at the beach break both left and right. "
                                    "Good "
                                    "surf at all stages of the tide. A fairly popluar wave that can sometimes get "
                                    "crowded "
                                    "Submerged rocks are a hazard.",
                        type_beach="Beach",
                        flag=2,
                        quality_when_it_works=2,
                        wave_consistency=2,
                        difficulty=3,
                        windsurf_y_kitesurf=3,
                        people_to_water=2,
                        sea_weends=3,
                        other_options=3,
                        water_quality=3,
                        access=3,
                        scenery=2,
                        local_attitude=1,
                        accommodation=3,
                        camping=5,
                        entertainment=3,
                        equipment_and_repairs=3,
                        restaurants=3,
                        pubs=3,
                        surf_fore_cast_link='<link href="//es.surf-forecast.com/stylesheets/widget.css" media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div class="widget-container"><div '
                                            'class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" '
                                            'src="//es.surf-forecast.com/breaks/La-Herradura-Andalucia/forecasts'
                                            '/widget/a '
                                            '" scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=36.73189781748929,
                        longitude=-3.7394453148970017
                    ),
                    Beach(
                        id=28,
                        name="La yerbabuena",
                        image="/statics/beaches/la_yerbabuena/la_yerbabuena_1.jpg",
                        description="La Yerbabuena in Andalucia is a fairly exposed point/rivermouth break that has "
                                    "unreliable waves. Summer in particular tends to be flat. The best wind direction "
                                    "is "
                                    "from the northeast. Most of the surf here comes from groundswells and the ideal "
                                    "swell angle is from the southwest. Often Crowded. Take special care here if it "
                                    "gets "
                                    "very crowded.",
                        type_beach="Point/Rivermouth",
                        flag=3,
                        quality_when_it_works=4,
                        wave_consistency=3,
                        difficulty=4,
                        windsurf_y_kitesurf=1,
                        people_to_water=3,
                        sea_weends=2,
                        other_options=4,
                        water_quality=5,
                        access=3,
                        scenery=5,
                        local_attitude=2,
                        accommodation=2,
                        camping=2,
                        entertainment=4,
                        equipment_and_repairs=1,
                        restaurants=5,
                        pubs=2,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div class="widget-container"><div '
                                            'class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" '
                                            'src="//www.surf-forecast.com/breaks/La-Yerbabuena/forecasts/widget/a" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=36.185640196516985,
                        longitude=-5.939918955975553
                    ),
                    Beach(
                        id=29,
                        name="Largos",
                        image="/statics/beaches/largos/largos_1.jpg",
                        description="Largos in Andalucia is an exposed reef break that only works when conditions are "
                                    "just right. Summer in particular tends to be flat. The best wind direction is "
                                    "from the "
                        "northwest with some shelter here from northeast winds. Short period wind swells are the rule "
                        "and the optimum wave angle is from the east southeast. No reef break here. Surfable at all "
                                    "stages of the tide. It's often crowded here. Watch out for rocks, urchins.",
                        type_beach="Reef",
                        flag=1,
                        quality_when_it_works=3,
                        wave_consistency=2,
                        difficulty=1,
                        windsurf_y_kitesurf=1,
                        people_to_water=2,
                        access=5,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div class="widget-container"><div '
                                            'class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" '
                                            'src="//www.surf-forecast.com/breaks/Largos/forecasts/widget/a" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        longitude=36.47316902844002,
                        latitude=-4.985158927836281,
                    ),
                    Beach(
                        id=30,
                        name="Marbella Playa del Cable",
                        image="/statics/beaches/marbella_playa_del_cable/marbella_playa_de_cable_1.jpg",
                        description="Marbella - Playa del Cable in Andalucia is an exposed beach break that does not "
                                    "work "
                                    "very often. Summer in particular tends to be flat. Works best in offshore winds "
                                    "from "
                                    "the north with some shelter here from west winds. The location means that "
                                    "groundswells are unknown and the best wave direction is from the east southeast. "
                                    "The "
                                    "beach break offers both left and right hand waves. The quality of the surf isn't "
                                    "affected by the tide. Likely to be crowded if working. Take special care here if "
                                    "it "
                                    "gets very crowded.",
                        type_beach="Beach",
                        flag=3,
                        quality_when_it_works=3,
                        wave_consistency=3,
                        difficulty=3,
                        windsurf_y_kitesurf=3,
                        people_to_water=3,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div class="widget-container"><div '
                                            'class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" '
                                            'src="//www.surf-forecast.com/breaks/Marbella-Playa-del-Cable/forecasts'
                                            '/widget/a" scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=36.50775553142923,
                        longitude=-4.869637833619527
                    ),
                    Beach(
                        id=31,
                        name="Matalascaña",
                        image="/statics/beaches/matalascañas/matalascañas_1.jpg",
                        description="Matalascañas in Andalucia is an exposed beach break that has quite reliable surf. "
                                    "Winter and spring are the best times of year to visit. The best wind direction is "
                                    "from the northeast. Windswells and groundswells in equal measure and the best "
                                    "swell "
                                    "direction is from the southwest. Waves at the beach break both left and right. "
                                    "Sometimes crowded. Surfing here means negotiating dangerous rips.",
                        type_beach="Beach",
                        flag=2,
                        quality_when_it_works=3,
                        wave_consistency=2,
                        difficulty=3,
                        windsurf_y_kitesurf=5,
                        people_to_water=4,
                        sea_weends=2,
                        other_options=2,
                        water_quality=3,
                        access=5,
                        scenery=4,
                        local_attitude=5,
                        accommodation=4,
                        camping=2,
                        entertainment=4,
                        equipment_and_repairs=2,
                        restaurants=5,
                        pubs=4,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div class="widget-container"><div '
                                            'class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" '
                                            'src="//www.surf-forecast.com/breaks/Matalascanas/forecasts/widget/a" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=36.992949608974236,
                        longitude=-6.547407797587745
                    ),
                    Beach(
                        id=32,
                        name="Mazagon",
                        image="/statics/beaches/mazagon/mazagon.jpg",
                        description="Mazagon in Andalucia is an exposed sandbar break that does not work very often. "
                                    "Winter and spring are the optimum times of year to visit. Offshore winds blow "
                                    "from "
                                    "the north northeast. Most of the surf here comes from groundswells and the ideal "
                                    "swell direction is from the southwest. Waves at the sandbar break both left and "
                                    "right. Best around low tide. Even when there are waves, it's not likley to be "
                                    "crowded.",
                        type_beach="Sandbar",
                        flag=3,
                        quality_when_it_works=2,
                        wave_consistency=2,
                        difficulty=3,
                        windsurf_y_kitesurf=2,
                        people_to_water=2,
                        access=4,
                        scenery=3,
                        local_attitude=2,
                        accommodation=3,
                        camping=3,
                        entertainment=3,
                        equipment_and_repairs=2,
                        restaurants=3,
                        pubs=3,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div class="widget-container"><div '
                                            'class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" '
                                            'src="//www.surf-forecast.com/breaks/Mazagon/forecasts/widget/a" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=37.127473269562145,
                        longitude=-6.816251775345296
                    ),
                    Beach(
                        id=33,
                        name="Mojacar",
                        image="/statics/beaches/moajacar/mojacar_1.jpg",
                        description="Mojacar in Andalucia is a reasonably exposed river break that only works once in "
                                    "a "
                                    "while. The best wind direction is from the northwest. The best swell direction is "
                                    "from the northwest. The river breaks offer lefts and rights. Good surf at all "
                                    "stages "
                                    "of the tide. A remote wave spot that never gets crowded. Beware of - Rocks - "
                                    "Man-made danger (buoys etc.).",
                        type_beach="River",
                        flag=2,
                        quality_when_it_works=2,
                        wave_consistency=2,
                        difficulty=2,
                        windsurf_y_kitesurf=2,
                        people_to_water=5,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div class="widget-container"><div '
                                            'class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" '
                                            'src="//www.surf-forecast.com/breaks/Mojacar-Beach-Pier/forecasts/widget'
                                            '/a" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=37.11610341497867,
                        longitude=-1.838788552679577
                    ),
                    Beach(
                        id=34,
                        name="Molino de papel",
                        image="/statics/beaches/molino_de_papel/molino_de_papel_1.jpg",
                        description="Molino de Papel in Andalucia is an exposed reef break that only works when "
                                    "conditions are just right. Summer in particular tends to be flat. Offshore winds "
                                    "blow from the north northeast. Short period wind swells are the rule and the "
                                    "ideal "
                                    "wave direction is from the south southwest. Good surf at all stages of the tide. "
                                    "When the surf is up, it can get quite busy in the water. Beware of - Urchins - "
                                    "Rocks "
                                    "- Localism - Pollution.",
                        type_beach="Reef",
                        flag=3,
                        quality_when_it_works=2,
                        wave_consistency=2,
                        difficulty=2,
                        windsurf_y_kitesurf=4,
                        people_to_water=5,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div class="widget-container"><div '
                                            'class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" '
                                            'src="//www.surf-forecast.com/breaks/Molino-de-Papel/forecasts/widget/a" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=36.751252508263065,
                        longitude=-3.816039514352716,
                    ),
                    Beach(
                        id=35,
                        name="Playa pico de el puerto",
                        image="/statics/beaches/playa_pico_del_puerto/playa_pico_del_puerto_1.jpg",
                        description="Pico de el Puerto in Andalucia is a fairly exposed reef break that only works "
                                    "when "
                                    "conditions are just right. Summer offers the best conditions for surfing. "
                                    "Offshore "
                                    "winds are from the west. The location means that groundswells are unknown and the "
                                    "optimum wave angle is from the east. There is a left breaking reef. Best around "
                                    "low "
                                    "tide. Relatively few surfers here, even on good days. Take care of rocks in the "
                                    "line "
                                    "up.",
                        type_beach="Reef",
                        flag=3,
                        quality_when_it_works=1,
                        wave_consistency=2,
                        difficulty=3,
                        windsurf_y_kitesurf=2,
                        people_to_water=4,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div class="widget-container"><div '
                                            'class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" '
                                            'src="//www.surf-forecast.com/breaks/Picodeel-Puerto/forecasts/widget/a" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=37.10026218786577,
                        longitude=-1.8321801291547135
                    ),
                    Beach(
                        id=36,
                        name="Pico de las cocheras",
                        image="/statics/beaches/pico_de_las_cocheras/pico_de_las_cocheras_1.jpg",
                        description="Pico de las Cocheras in Andalucia is a reasonably exposed beach break that has "
                                    "inconsistent surf. Summer offers the best conditions for surfing. The best wind "
                                    "direction is from the west. Windswells provide any waves and the best wave "
                                    "direction "
                                    "is from the east. The beach break offers both left and right hand waves. Best "
                                    "around "
                                    "low tide. Relatively few surfers here, even on good days. Submerged rocks are a "
                                    "hazard.",
                        type_beach="Beach",
                        flag=3,
                        quality_when_it_works=1,
                        wave_consistency=2,
                        difficulty=1,
                        windsurf_y_kitesurf=2,
                        people_to_water=4,
                        water_quality=4,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div class="widget-container"><div '
                                            'class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" '
                                            'src="//www.surf-forecast.com/breaks/Picodelas-Cocheras/forecasts/widget'
                                            '/a" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=36.74467175133951,
                        longitude=-2.1174040371064256
                    ),
                    Beach(
                        id=37,
                        name="Playa central",
                        image="/statics/beaches/playa_central/playa_central_1.jpg",
                        description="Playa Central in Andalucia is a reasonably exposed beach break that has fairly "
                                    "consistent surf. Winter and spring are the optimum times of year to visit. Works "
                                    "best in offshore winds from the north northwest. Most of the surf here comes from "
                                    "groundswells and the best swell direction is from the south southeast. The beach "
                                    "break offers both left and right hand waves. When it's working here, it can get "
                                    "crowded. Take care of Pollution.",
                        type_beach="Beach",
                        flag=2,
                        quality_when_it_works=1,
                        wave_consistency=1,
                        difficulty=2,
                        windsurf_y_kitesurf=2,
                        people_to_water=4,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div class="widget-container"><div '
                                            'class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" '
                                            'src="//www.surf-forecast.com/breaks/Isla-Cristina/forecasts/widget/a" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=37.19557111601737,
                        longitude=-7.304793462359088
                    ),
                    Beach(
                        id=38,
                        name="Playa de la carchuna",
                        image="/statics/beaches/playa_de_la_carchuna/playa_de_la_carchuna_1.jpg",
                        description="Playa de Carchuna(Calahonda) in Andalucia is an exposed beach break. Summer "
                                    "offers "
                                    "the best conditions for surfing. Works best in offshore winds from the north. "
                                    "Short "
                                    "period wind swells are the rule and the optimum wave angle is from the southwest. "
                                    "The beach breaks offers right-handers. Best around low tide. Relatively few "
                                    "surfers "
                                    "here, even on good days. Watch out for rocks.",
                        type_beach="Beach",
                        flag=3,
                        quality_when_it_works=3,
                        wave_consistency=2,
                        difficulty=4,
                        windsurf_y_kitesurf=3,
                        people_to_water=4,
                        other_options=3,
                        water_quality=3,
                        access=4,
                        scenery=3,
                        local_attitude=3,
                        accommodation=3,
                        camping=3,
                        entertainment=3,
                        equipment_and_repairs=2,
                        restaurants=3,
                        pubs=3,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div class="widget-container"><div '
                                            'class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" '
                                            'src="//www.surf-forecast.com/breaks/Isla-Cristina/forecasts/widget/a" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=36.69512890441411,
                        longitude=-3.457206445803679
                    ),
                    Beach(
                        id=39,
                        name="Playa de la Canaleta",
                        image="/statics/beaches/playa_de_la_canaleta/playa_de_la_canaleta_1.jpg",
                        description="Playa de la Canaleta in Andalucia is an exposed beach break that has pretty "
                                    "consitent surf. Winter and spring are the optimum times of year to visit. "
                                    "Offshore "
                                    "winds blow from the northeast. Tends to receive a mix of groundswells and "
                                    "windswells "
                                    "and the ideal swell direction is from the southwest. Waves at the beach break "
                                    "both "
                                    "left and right. Sometimes crowded. Dangerous rips are a hazard of surfing here.",
                        type_beach="Beach",
                        flag=3,
                        quality_when_it_works=3,
                        wave_consistency=3,
                        difficulty=2,
                        windsurf_y_kitesurf=3,
                        people_to_water=4,
                        sea_weends=3,
                        other_options=5,
                        water_quality=3,
                        access=5,
                        scenery=3,
                        local_attitude=5,
                        accommodation=2,
                        camping=3,
                        entertainment=3,
                        equipment_and_repairs=2,
                        restaurants=2,
                        pubs=4,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div class="widget-container"><div '
                                            'class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" '
                                            'src="//www.surf-forecast.com/breaks/La-Canaleta/forecasts/widget/m" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=37.173765347014374,
                        longitude=-6.949949449584676
                    ),
                    Beach(
                        id=40,
                        name="Playa de Regla",
                        image="/statics/beaches/playa_de_regla/playa_de_regla_1.jpg",
                        description="Playa de Regla in Andalucia is an exposed beach break that usually has waves. "
                                    "Winter "
                                    "and spring are the optimum times of year to visit. Offshore winds are from the "
                                    "east. "
                                    "Windswells and groundswells in equal measure and the ideal swell direction is "
                                    "from "
                                    "the west southwest. The beach break provides left and right handers. Often "
                                    "Crowded.",
                        type_beach="Beach",
                        flag=2,
                        quality_when_it_works=4,
                        wave_consistency=3,
                        difficulty=3,
                        windsurf_y_kitesurf=4,
                        people_to_water=3,
                        sea_weends=3,
                        other_options=5,
                        water_quality=3,
                        access=5,
                        scenery=4,
                        local_attitude=2,
                        accommodation=5,
                        camping=2,
                        entertainment=3,
                        equipment_and_repairs=1,
                        restaurants=3,
                        pubs=3,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div class="widget-container"><div '
                                            'class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" '
                                            'src="//www.surf-forecast.com/breaks/Playade-Regla/forecasts/widget/m" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=36.72594424375206,
                        longitude=-6.4398987214667525
                    ),
                    Beach(
                        id=41,
                        name="Playa de las tres piedras",
                        image="/statics/beaches/playa_de_las_tres_piedras/playa_de_las_tres_piedras_1.jpg",
                        description="Playa de Tres Piedras in Andalucia is an exposed beach break that has dependable "
                                    "surf. Winter and spring are the optimum times of year to visit. Offshore winds "
                                    "blow "
                                    "from the east northeast. Tends to receive a mix of groundswells and windswells "
                                    "and "
                                    "the best swell direction is from the west southwest. The beach breaks offer lefts "
                                    "and rights. When the surf is up, crowds are likely Take care of rocks in the line "
                                    "up.",
                        type_beach="Beach",
                        flag=2,
                        quality_when_it_works=3,
                        wave_consistency=3,
                        difficulty=2,
                        windsurf_y_kitesurf=4,
                        people_to_water=3,
                        sea_weends=3,
                        other_options=3,
                        water_quality=4,
                        access=5,
                        scenery=4,
                        local_attitude=4,
                        accommodation=3,
                        camping=4,
                        entertainment=3,
                        equipment_and_repairs=2,
                        restaurants=4,
                        pubs=4,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" rel="stylesheet" type="text/css" /><div '
                                            'class="wf-width-cont '
                                            'surf-fc-widget"><div class="widget-container"><div '
                                            'class="external-cont"><iframe '
                                            'class="surf-fc-i" allowtransparency="true" '
                                            'src="//www.surf-forecast.com/breaks/Playade-Tres-Piedras/forecasts'
                                            '/widget/a" scrolling="no" '
                                            'frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=36.702412289228704,
                        longitude=-6.429632493696671
                    ),
                    Beach(
                        id=42,
                        name="Playa del Bombo",
                        image="/statics/beaches/playa_del_bombo/playa_del_bombo_1.jpg",
                        description="Playa el Bombo in Andalucia is an exposed beach break that has unreliable waves "
                                    "with "
                                    "no particular seasonal pattern. Works best in offshore winds from the northwest. "
                                    "The "
                                    "short fetch makes for windswells rather than groundswells and the optimum wave "
                                    "angle "
                                    "is from the east southeast. The beach break offers both left and right hand "
                                    "waves. "
                                    "Good surf at all stages of the tide. Sometimes crowded. Rocks are a hazard",
                        type_beach="Beach",
                        flag=3,
                        quality_when_it_works=3,
                        wave_consistency=2,
                        difficulty=4,
                        windsurf_y_kitesurf=3,
                        people_to_water=3,
                        sea_weends=3,
                        other_options=3,
                        water_quality=4,
                        access=5,
                        scenery=3,
                        local_attitude=5,
                        accommodation=5,
                        camping=2,
                        equipment_and_repairs=1,
                        restaurants=5,
                        pubs=2,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div class="widget-container"><div '
                                            'class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" '
                                            'src="//www.surf-forecast.com/breaks/Playa-El-Bombo/forecasts/widget/m" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=36.49524585538715,
                        longitude=-4.688538239814334
                    ),
                    Beach(
                        id=43,
                        name="Playa la Carihuela",
                        image="/statics/beaches/playa_la_carihuela/playa_la_carihuela_1.jpg",
                        description="Playa la Carihuela in Andalucia is an exposed beach break that has inconsistent "
                                    "surf. Winter is the favoured time of year for surfing here. The best wind "
                                    "direction "
                                    "is from the northwest. There is too little fetch for groundswells to form and the "
                                    "best wave direction is from the southeast. The beach break provides left and "
                                    "right "
                                    "handers. Best around mid tide. Even when there are waves, it's not likley to be "
                                    "crowded. Watch out for dangerous rips.",
                        type_beach="Beach",
                        flag=2,
                        quality_when_it_works=3,
                        wave_consistency=3,
                        difficulty=2,
                        windsurf_y_kitesurf=2,
                        people_to_water=3,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div class="widget-container"><div '
                                            'class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" '
                                            'src="//www.surf-forecast.com/breaks/Playala-Carihuela/forecasts/widget/m" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=36.60801350151034,
                        longitude=-4.50465180832617
                    ),
                    Beach(
                        id=44,
                        name="Puerto Cabopino",
                        image="/statics/beaches/puerto_cabopino/puerto_cabopino_1.jpg",
                        description="Puerto Cabopino in Andalucia is an exposed sandbar break that has reasonably "
                                    "consistent surf and can work at any time of the year. Offshore winds are from the "
                                    "north. Most of the surf comes fis in the form of windswells and the best wave "
                                    "direction is from the east southeast. The sandbar breaks offer lefts and rights. "
                                    "When the surf is up, it can get quite busy in the water. Rocks are a hazard.",
                        type_beach="Sandbar",
                        flag=3,
                        quality_when_it_works=3,
                        wave_consistency=3,
                        difficulty=2,
                        windsurf_y_kitesurf=5,
                        people_to_water=2,
                        sea_weends=4,
                        other_options=3,
                        water_quality=4,
                        access=5,
                        scenery=5,
                        local_attitude=4,
                        accommodation=4,
                        camping=4,
                        entertainment=4,
                        equipment_and_repairs=2,
                        restaurants=5,
                        pubs=4,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div class="widget-container"><div '
                                            'class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" '
                                            'src="//www.surf-forecast.com/breaks/Cabopino/forecasts/widget/a" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe>></div></div></div>',
                        latitude=36.484043196372944,
                        longitude=-4.742735787143768
                    ),
                    Beach(
                        id=45,
                        name="Puerto Marina",
                        image="/statics/beaches/puerto_marina/puerto_marina_1.jpg",
                        description="Puerto Marina in Andalucia is a fairly exposed sandbar break that has "
                                    "inconsistent "
                                    "surf. Autumn and winter are the optimum times of year for waves. Works best in "
                                    "offshore winds from the north northwest with some shelter here from southwest "
                                    "winds. "
                                    "Most of the surf comes fis in the form of windswells and the best wave direction "
                                    "is "
                                    "from the southeast. The sandbar break provides left and right handers. Surfable "
                                    "at "
                                    "all stages of the tide. It's often crowded here.",
                        type_beach="Sandbar",
                        flag=2,
                        quality_when_it_works=3,
                        wave_consistency=3,
                        difficulty=2,
                        windsurf_y_kitesurf=1,
                        people_to_water=2,
                        sea_weends=2,
                        other_options=3,
                        water_quality=4,
                        access=5,
                        scenery=3,
                        local_attitude=3,
                        accommodation=5,
                        camping=1,
                        entertainment=3,
                        equipment_and_repairs=1,
                        restaurants=5,
                        pubs=5,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div class="widget-container"><div '
                                            'class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" '
                                            'src="//www.surf-forecast.com/breaks/Puerto-Marina/forecasts/widget/m" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=36.59454561496709,
                        longitude=-4.517799185599584
                    ),
                    Beach(
                        id=46,
                        name="Punta del Moral",
                        image="/statics/beaches/punta_del_moral/punta_del_moral_1.jpg",
                        description="Punta del Moral in Andalucia is a quite exposed beach and breakwater break that "
                                    "has "
                                    "fairly consistent surf. Winter and spring are the favoured times of year to "
                                    "visit. "
                                    "Offshore winds are from the north northwest. Waves just as likely from local "
                                    "windswells as from distant groundswells and the best swell direction is from the "
                                    "south southeast. The beach break provides left and right handers. A fairly "
                                    "popluar "
                                    "wave that can sometimes get crowded Beware of Pollution.",
                        type_beach="Beach and Breakwater",
                        flag=3,
                        quality_when_it_works=2,
                        wave_consistency=2,
                        difficulty=2,
                        windsurf_y_kitesurf=3,
                        people_to_water=3,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div class="widget-container"><div '
                                            'class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" '
                                            'src="//www.surf-forecast.com/breaks/Punta-del-Moral/forecasts/widget/a" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=37.16890500685277,
                        longitude=-7.386827250388443
                    ),
                    Beach(
                        id=47,
                        name="Playa Umbria",
                        image="/statics/beaches/playa_umbria/playa_umbria_1.jpg",
                        description="Punta Umbria (Playa Camarón) in Andalucia is an exposed beach break that has "
                                    "fairly consistent surf. Winter and spring are the favoured times of year to "
                                    "visit. Works "
                                    "best in offshore winds from the northeast. Tends to receive a mix of "
                                    "groundswells and "
                                    "windswells and the best swell direction is from the southwest. The beach break "
                                    "provides left "
                                    "and right handers. It's sometimes crowded here. Surfing here means negotiating "
                                    "dangerous "
                                    "rips.",
                        type_beach="Beach",
                        flag=3,
                        quality_when_it_works=3,
                        wave_consistency=3,
                        difficulty=2,
                        windsurf_y_kitesurf=4,
                        people_to_water=3,
                        sea_weends=2,
                        other_options=3,
                        water_quality=3,
                        access=5,
                        scenery=5,
                        local_attitude=5,
                        accommodation=5,
                        camping=2,
                        entertainment=5,
                        equipment_and_repairs=3,
                        restaurants=5,
                        pubs=4,
                        surf_fore_cast_link='<link href="//www.surf-forecast.com/stylesheets/widget.css" '
                                            'media="screen" '
                                            'rel="stylesheet" type="text/css" /><div class="wf-width-cont '
                                            'surf-fc-widget"><div class="widget-container"><div '
                                            'class="external-cont"><iframe class="surf-fc-i" allowtransparency="true" '
                                            'src="//www.surf-forecast.com/breaks/Playa-El-Camaron/forecasts/widget/a" '
                                            'scrolling="no" frameborder="0" marginwidth="0" '
                                            'marginheight="0"></iframe></div></div></div>',
                        latitude=36.718360149496434,
                        longitude=-6.440367121843422
                    )
                ]
            )
            db.session.commit()
