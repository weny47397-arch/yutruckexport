#!/usr/bin/env python3
"""Build 8 country pages for SHACMAN trucks Africa markets — Phase 2 personalised."""

# Each country now has differentiated:
# - hero_title, hero_sub (specific selling proposition)
# - port, port_detail
# - market_data (real 2024-2025 facts)
# - buyer_types (3-4 typical buyers)
# - common_applications (specific to that country)
# - recommended_trucks (NOT always the same — varies by use case)
# - shipping_days (real shipping time from Chinese ports)
# - import_notes (form E, AGOA, customs notes)
# - faq (3-4 country-specific FAQs)

COUNTRIES = [
    {
        "slug": "tanzania",
        "name": "Tanzania",
        "flag": "🇹🇿",
        "hero_title": "SHACMAN Trucks for Tanzania's East African Logistics Hub",
        "hero_sub": "Dump trucks, tractor trucks and cargo trucks shipped from China to Dar es Salaam. SHACMAN opened its East Africa flagship dealership in Arusha in mid-2025 — your local parts and service support is now ready.",
        "port": "Dar es Salaam",
        "port_detail": "Tanzania's main seaport serves as the gateway to landlocked neighbours: DRC, Rwanda, Burundi, Uganda, and Zambia's northern corridor.",
        "market_data": [
            ("Truck fleet size", "~26,000 heavy-duty trucks (2024 estimate)"),
            ("Main highway", "Dar es Salaam — Dodoma — Arusha — Kenya border"),
            ("SHACMAN local presence", "Arusha East Africa dealership opened June 2025 (Prime Minister officiated)"),
            ("Best-selling models", "6×4 tractor head, 6×4 dump, 8×4 rigid"),
        ],
        "buyer_types": [
            ("Container hauliers", "Moving 20ft/40ft containers from Dar es Salaam port to inland destinations"),
            ("Mining logistics", "Supply to Geita, Bulyanhulu, North Mara gold mines; Tanzanite mining in Mererani"),
            ("Construction fleets", "Public works — roads, railways (SGR), Standard Gauge Railway project supply"),
            ("Cross-border traders", "Tanzania → DRC, Zambia, Rwanda cross-border cargo"),
        ],
        "common_applications": "Container haulage from port to inland destinations, mining supply routes in Geita and Bulyanhulu, SGR and infrastructure project logistics, cross-border freight to DRC and Rwanda.",
        "shipping_days": "20–25 days",
        "import_notes": [
            "Form E (EAC Certificate of Origin) accepted — partial duty reduction",
            "Tanzania Bureau of Standards (TBS) pre-shipment inspection required",
            "TRA (Tanzania Revenue Authority) handles customs clearance at Dar es Salaam",
        ],
        "recommended_trucks": [
            {"img": "shacman-f3000-6x4-highway.jpg", "type": "DUMP TRUCK", "name": "SHACMAN F3000 6×4 Dump Truck", "desc": "Workhorse for Geita gold mines and Mererani tanzanite — reinforced chassis for unpaved haul roads.", "link": "products/f-series.html"},
            {"img": "shacman-x3000-6x4-tractor.jpg", "type": "TRACTOR HEAD", "name": "SHACMAN X3000 6×4 Tractor Head", "desc": "Container haulage from Dar es Salaam port — flagship cabin for driver comfort on long routes.", "link": "products/x3000.html"},
            {"img": "shacman-l3000-6x4-cargo.jpg", "type": "CARGO TRUCK", "name": "SHACMAN L3000 6×4 Cargo Truck", "desc": "Regional distribution and cross-border cargo to Rwanda, Burundi, western Uganda.", "link": "products/l3000.html"},
        ],
        "faqs": [
            ("Do you deliver CIF to Dar es Salaam?", "Yes. We arrange CIF shipping to Dar es Salaam port, including insurance. For door delivery to inland destinations (Dodoma, Arusha, Mwanza), we work with local logistics partners."),
            ("Is SHACMAN supported locally in Tanzania?", "Yes — SHACMAN opened its East Africa flagship dealership in Arusha in June 2025, with parts inventory and service technicians. Spare parts supply is now faster than direct-from-China."),
            ("What's the import duty on trucks in Tanzania?", "Import duty is typically 25% + VAT 18% + withholding tax 2%. With Form E (EAC origin certificate), the duty can be reduced to 0% for raw materials — we assist with the documentation."),
        ],
    },
    {
        "slug": "zambia",
        "name": "Zambia",
        "flag": "🇿🇲",
        "hero_title": "SHACMAN Trucks for Zambia's Copper Belt Mining",
        "hero_sub": "Heavy-duty dump trucks and tractor heads for Zambia's copper, cobalt, and cross-border logistics. Lobito Corridor opens a new Atlantic route for SHACMAN exports to Zambia.",
        "port": "Dar es Salaam / Walvis Bay",
        "port_detail": "Two main routes into Zambia: Dar es Salaam via Tanzam Highway (T2) to Kapiri Mposhi, or Walvis Bay via the Trans-Kalahari Corridor through Namibia.",
        "market_data": [
            ("Truck fleet size", "~12,000 heavy-duty trucks serving Copper Belt"),
            ("Main mining hub", "Kitwe, Ndola, Lubumbashi border, Lumwana, Solwezi"),
            ("New corridor", "Lobito Corridor (Angola Atlantic port) — first rail shipment 2024"),
            ("Best-selling models", "F3000 6×4 mining dump, X3000 6×6 mining"),
        ],
        "buyer_types": [
            ("Copper miners", "First Quantum, Barrick Lumwana, Mopani, KCM — mining haulage contracts"),
            ("Cobalt logistics", "DRC-Zambia cross-border cobalt and copper concentrate transport"),
            ("Cross-border hauliers", "Truckers running T2 (Dar-Kapiri) and Walvis Bay corridors"),
            ("Construction fleets", "Road construction, hydropower projects"),
        ],
        "common_applications": "Copper and cobalt haulage from Copper Belt mines, cross-border logistics via Walvis Bay and Lobito corridors, heavy-duty mining dump operations, road construction and hydropower projects.",
        "shipping_days": "30–40 days",
        "import_notes": [
            "COMESA Certificate of Origin — preferential access for SHACMAN imports",
            "Zambia Revenue Authority (ZRA) handles customs at Nakonde, Kazungula, Chirundu borders",
            "Engineering Council of Zambia registration required for fleet operators",
        ],
        "recommended_trucks": [
            {"img": "shacman-f3000-6x4-highway.jpg", "type": "MINING DUMP", "name": "SHACMAN F3000 6×4 Heavy Dump Truck", "desc": "Reinforced chassis for Copper Belt mine haul roads — 30-ton payload, Cummins ISM engine, tropical cooling.", "link": "products/f-series.html"},
            {"img": "shacman-x3000-6x4-tractor.jpg", "type": "TRACTOR HEAD", "name": "SHACMAN X3000 6×4 Tractor Head", "desc": "Walvis Bay → Lusaka long-haul. Reinforced cab suspension for corrugated road sections.", "link": "products/x3000.html"},
            {"img": "shacman-x3000-6x4-mining.jpg", "type": "MINING SPECIAL", "name": "SHACMAN X3000 6×6 Mining Tipper", "desc": "Heavy mining configuration for First Quantum / Barrick Lumwana sites — extra drive axle for steep ramps.", "link": "products/x3000.html"},
        ],
        "faqs": [
            ("Is SHACMAN common in Zambia's mines?", "Yes — SHACMAN has been used by major operators in the Copper Belt, including First Quantum's Sentinel mine and Barrick's Lumwana. Parts supply via Johannesburg and Dubai corridors."),
            ("What's the Lobito Corridor?", "A new rail route from DRC copper mines through Angola to the Atlantic port of Lobito. SHACMAN tractor heads are increasingly used to support this route from the Zambia/DRC side."),
            ("How long does shipping take to Walvis Bay?", "40–45 days from Shanghai/Tianjin via Cape of Good Hope. We can also arrange RoRo service for faster delivery."),
        ],
    },
    {
        "slug": "kenya",
        "name": "Kenya",
        "flag": "🇰🇪",
        "hero_title": "SHACMAN Trucks for Kenya — Mombasa Port Hub",
        "hero_sub": "SHACMAN established regional assembly hubs in Nairobi and Mombasa. Tractor heads and dump trucks for East Africa's largest re-export corridor.",
        "port": "Mombasa",
        "port_detail": "Mombasa port serves Kenya, Uganda, Rwanda, South Sudan, and eastern DRC. The Mombasa-Nairobi highway (A109) handles the largest share of heavy truck traffic in East Africa.",
        "market_data": [
            ("Port throughput", "Mombasa handles ~1.5 million TEU annually — largest in East Africa"),
            ("SHACMAN local presence", "Regional assembly hubs in Nairobi and Mombasa (announced 2024)"),
            ("Main highway", "Mombasa — Nairobi — Uganda/Rwanda border"),
            ("Best-selling models", "X3000 6×4 tractor, F3000 6×4 dump, H3000 tanker"),
        ],
        "buyer_types": [
            ("Container hauliers", "Moving containers from Mombasa port to Nairobi and across borders"),
            ("Long-distance traders", "Kenya → Uganda, Rwanda, South Sudan cross-border freight"),
            ("Cement and construction", "Cement, steel, infrastructure material logistics"),
            ("Agricultural logistics", "Tea, coffee, horticultural produce to port"),
        ],
        "common_applications": "Container haulage from Mombasa port, cross-border logistics to Uganda and Rwanda, cement and construction material transport, agricultural produce to port.",
        "shipping_days": "20–25 days",
        "import_notes": [
            "EAC Certificate of Origin (Form E) — preferential tariff treatment",
            "Kenya Bureau of Standards (KEBS) pre-shipment verification (PVoC)",
            "KRA (Kenya Revenue Authority) handles customs clearance",
        ],
        "recommended_trucks": [
            {"img": "shacman-x3000-6x4-tractor.jpg", "type": "TRACTOR HEAD", "name": "SHACMAN X3000 6×4 Tractor Head", "desc": "Flagship for Mombasa-Nairobi-Kampala route. 460 hp Weichai, intelligent fuel management.", "link": "products/x3000.html"},
            {"img": "shacman-f3000-6x4-highway.jpg", "type": "DUMP TRUCK", "name": "SHACMAN F3000 6×4 Dump Truck", "desc": "SGR railway project supply, road construction, building material haulage.", "link": "products/f-series.html"},
            {"img": "shacman-h3000-6x4-tractor.jpg", "type": "TANKER", "name": "SHACMAN H3000 6×4 Fuel Tanker", "desc": "Petroleum distribution from Mombasa port and inland depots.", "link": "products/h3000.html"},
        ],
        "faqs": [
            ("Does SHACMAN have local assembly in Kenya?", "SHACMAN announced regional assembly hubs in Nairobi and Mombasa in 2024. This brings faster delivery and lower CIF costs for Kenyan customers."),
            ("What's the typical shipping time from China to Mombasa?", "20–25 days from Shanghai or Tianjin. RoRo vessels carry trucks directly to Mombasa."),
            ("Do you handle KEBS PVoC certification?", "Yes — we coordinate pre-shipment verification with KEBS for your order. This avoids customs delays at Mombasa."),
        ],
    },
    {
        "slug": "cameroon",
        "name": "Cameroon",
        "flag": "🇨🇲",
        "hero_title": "SHACMAN Trucks for Cameroon — Central Africa Gateway",
        "hero_sub": "Tractor heads and dump trucks for the Douala-N'Djamena corridor — 20,000 truck movements a year between Cameroon and Chad alone.",
        "port": "Douala",
        "port_detail": "Douala port is the gateway to Central Africa, serving Cameroon, Chad, Central African Republic, and northern Republic of Congo.",
        "market_data": [
            ("Corridor volume", "20,000+ truck movements a year to Chad (Cameroon Customs, 2024)"),
            ("Corridor revenue", "CFA 350 billion+ annual transit revenue from Chadian goods"),
            ("Main highway", "Douala — Yaoundé — N'Djamena (1,800 km strategic corridor)"),
            ("EU project", "Modernisation of N'Djamena-Douala corridor (Q2 2024 onwards)"),
        ],
        "buyer_types": [
            ("Chadian hauliers", "Truckers moving goods from Douala port to N'Djamena and other Chad destinations"),
            ("Hydrocarbon logistics", "Oil and petroleum transport to Chad and CAR"),
            ("Timber and agri logistics", "Cocoa, coffee, timber transport"),
            ("Public works fleets", "Infrastructure and road construction projects"),
        ],
        "common_applications": "Container haulage from Douala port to Chad corridor, hydrocarbon transport, timber and agricultural logistics, public infrastructure projects.",
        "shipping_days": "35–45 days",
        "import_notes": [
            "CEMAC region — Cameroon, Chad, CAR, Congo, Gabon, Equatorial Guinea share customs rules",
            "Douane Camerounaise handles customs clearance",
            "Cameroon Conformity Assessment Programme (CAMACO) pre-shipment inspection for some goods",
        ],
        "recommended_trucks": [
            {"img": "shacman-x3000-6x4-tractor.jpg", "type": "TRACTOR HEAD", "name": "SHACMAN X3000 6×4 Tractor Head", "desc": "Long-haul Douala → N'Djamena. Reinforced cooling for tropical climate, 550 hp option.", "link": "products/x3000.html"},
            {"img": "shacman-f3000-6x4-highway.jpg", "type": "DUMP TRUCK", "name": "SHACMAN F3000 6×4 Dump Truck", "desc": "Construction material and infrastructure projects in Douala, Yaoundé.", "link": "products/f-series.html"},
            {"img": "shacman-h3000-6x4-tractor.jpg", "type": "FUEL TANKER", "name": "SHACMAN H3000 6×4 Fuel Tanker", "desc": "Hydrocarbon distribution to Chad via the corridor. Aluminium tank option available.", "link": "products/h3000.html"},
        ],
        "faqs": [
            ("Can you deliver to N'Djamena (Chad)?", "Yes. We arrange CIF Douala, then we work with local partners to clear transit through Cameroon's customs to N'Djamena. Cameroon-Chad corridor modernisation project is ongoing with EU funding."),
            ("What's the import duty in Cameroon?", "Cameroon applies CEMAC Common External Tariff (CET) — typically 20% duty + 19.25% VAT for trucks. We can assist with documentation."),
            ("What about French-speaking support?", "Yes — Yu coordinates in English, and our local partners in Douala provide French-speaking support for Cameroon, Chad, CAR customers."),
        ],
    },
    {
        "slug": "ghana",
        "name": "Ghana",
        "flag": "🇬🇭",
        "hero_title": "SHACMAN Trucks for Ghana — Tema Port Mining Hub",
        "hero_sub": "SHACMAN dump trucks from $30k for Ghana's gold, bauxite and manganese mines. Tema port also serves landlocked Burkina Faso and Mali.",
        "port": "Tema",
        "port_detail": "Tema port is Ghana's main seaport, serving Accra metropolitan area, plus transit trade to Burkina Faso, Mali, and Niger via the Tema-Ouagadougou corridor.",
        "market_data": [
            ("Port throughput", "Tema handles ~1.4 million TEU annually (2024)"),
            ("Mining areas", "Obuasi (AngloGold Ashanti), Tarkwa, Ahafo, Awaso (bauxite), Nsuta (manganese)"),
            ("Best-selling SHACMAN", "F3000 6×4 dump truck (~$30,000 new)"),
            ("Top brands in market", "SHACMAN, SINOTRUK HOWO, FAW, Dongfeng"),
        ],
        "buyer_types": [
            ("Small-scale miners", "Artisanal and small-scale gold mining — single truck buyers"),
            ("Large mining fleets", "AngloGold Ashanti, Newmont Ghana — fleet contracts"),
            ("Burkina Faso / Mali traders", "Cross-border re-export of trucks and parts"),
            ("Construction fleets", "Accra and Kumasi road and building projects"),
        ],
        "common_applications": "Mining haulage (gold, bauxite, manganese), container haulage from Tema port, agricultural logistics (cocoa, timber), construction material transport.",
        "shipping_days": "30–35 days",
        "import_notes": [
            "Ghana Revenue Authority (GRA) handles customs at Tema",
            "Destination Inspection (DI) scheme — pre-shipment inspection mandatory",
            "Ghana Standards Authority (GSA) conformity assessment for used vehicles (new trucks generally exempt)",
        ],
        "recommended_trucks": [
            {"img": "shacman-f3000-6x4-highway.jpg", "type": "DUMP TRUCK", "name": "SHACMAN F3000 6×4 Dump Truck", "desc": "The most popular SHACMAN in Ghana — used in Obuasi, Tarkwa and small-scale mines. From ~$30,000 new.", "link": "products/f-series.html"},
            {"img": "shacman-x3000-6x4-tractor.jpg", "type": "TRACTOR HEAD", "name": "SHACMAN X3000 6×4 Tractor Head", "desc": "Container haulage Tema → Accra → Burkina Faso (Ouagadougou, Bobo-Dioulasso).", "link": "products/x3000.html"},
            {"img": "shacman-h3000-6x4-tractor.jpg", "type": "TANKER", "name": "SHACMAN H3000 6×4 Tanker", "desc": "Water and fuel distribution for mining sites in Western Region.", "link": "products/h3000.html"},
        ],
        "faqs": [
            ("Why is SHACMAN popular in Ghana?", "SHACMAN offers competitive pricing (from $30k for new dump trucks) and a strong presence in the Tema dealer network. Spare parts are widely available."),
            ("Do you ship CIF Tema?", "Yes. CIF Tema is our standard term for Ghana. We work with Tema port agents for customs clearance."),
            ("Can I buy just one truck?", "Yes — MOQ is 1 unit for SHACMAN. Single-truck buyers are common from Ghana's small-scale mining sector."),
        ],
    },
    {
        "slug": "nigeria",
        "name": "Nigeria",
        "flag": "🇳🇬",
        "hero_title": "SHACMAN Trucks for Nigeria — Lagos and Onne Ports",
        "hero_sub": "Heavy-duty dump trucks and tractor heads for Africa's largest economy. SHACMAN ranks among the top Chinese brands alongside SINOTRUK HOWO in Nigerian mining and construction.",
        "port": "Lagos / Onne",
        "port_detail": "Two main seaports: Lagos (Apapa and Tin Can Island) for the commercial capital, and Onne Port for the oil-producing south-east (Port Harcourt region).",
        "market_data": [
            ("Truck market size", "Nigeria is the largest truck market in West Africa by volume"),
            ("Top Chinese brands", "SINOTRUK HOWO, SHACMAN, FAW, Dongfeng, Foton"),
            ("SONCAP", "Mandatory pre-shipment conformity for all imports"),
            ("Customs challenge", "PAAR (Pre-Arrival Assessment Report) required at Lagos and Tin Can"),
        ],
        "buyer_types": [
            ("Mining contractors", "Solid minerals — gold, limestone, coal — Abuja, Jos, Enugu corridors"),
            ("Oil & gas logistics", "Niger Delta field logistics, rig supply, fuel transport"),
            ("Interstate hauliers", "Lagos ↔ Abuja, Lagos ↔ Port Harcourt, Lagos ↔ Kano long-distance"),
            ("Construction fleets", "Lagos, Abuja infrastructure, real estate development"),
        ],
        "common_applications": "Heavy construction in Lagos and Abuja, oil & gas field logistics in the Niger Delta, interstate haulage across the country, container distribution from Lagos and Onne ports.",
        "shipping_days": "30–40 days",
        "import_notes": [
            "SONCAP (Standards Organisation of Nigeria Conformity Assessment Programme) — mandatory",
            "PAAR (Pre-Arrival Assessment Report) — required before shipment arrives",
            "Nigerian Customs Service handles clearance at Apapa, Tin Can, Onne",
        ],
        "recommended_trucks": [
            {"img": "shacman-f3000-6x4-highway.jpg", "type": "DUMP TRUCK", "name": "SHACMAN F3000 6×4 Dump Truck", "desc": "Lagos and Abuja construction, Jos and Enugu mining. Cummins engine, 30-ton payload.", "link": "products/f-series.html"},
            {"img": "shacman-x3000-6x4-tractor.jpg", "type": "TRACTOR HEAD", "name": "SHACMAN X3000 6×4 Tractor Head", "desc": "Interstate haulage Lagos-Abuja-Kano. Euro II/III compliant for Nigerian emission standards.", "link": "products/x3000.html"},
            {"img": "shacman-h3000-6x4-tractor.jpg", "type": "FUEL TANKER", "name": "SHACMAN H3000 6×4 Fuel Tanker", "desc": "Niger Delta petroleum logistics. Aluminium tank for safe hydrocarbon transport.", "link": "products/h3000.html"},
        ],
        "faqs": [
            ("Does SHACMAN sell well in Nigeria?", "SHACMAN is among the top 5 Chinese brands in Nigeria — particularly strong in mining and heavy construction. It competes closely with SINOTRUK HOWO in the same segment."),
            ("What is SONCAP and do you handle it?", "SONCAP is the mandatory pre-shipment conformity assessment. We coordinate SONCAP certification for your order so your trucks clear Nigerian customs smoothly."),
            ("What's the typical shipping time to Lagos?", "30–40 days from Chinese ports. We can also arrange consolidation with other buyers to reduce CIF cost for smaller orders."),
        ],
    },
    {
        "slug": "drc",
        "name": "DR Congo",
        "flag": "🇨🇩",
        "hero_title": "SHACMAN Trucks for DR Congo — Katanga Copper Belt",
        "hero_sub": "Heavy-duty mining dump trucks and tractor heads for the world's largest cobalt producer. The Katanga–Dar es Salaam corridor is 2,000 km of constant truck traffic.",
        "port": "Matadi / Dar es Salaam",
        "port_detail": "Two main access routes: Matadi port on the Atlantic for western DRC, and Dar es Salaam (Tanzania) for the copper belt (Katanga). The Dar route handles most heavy mining haulage.",
        "market_data": [
            ("Mining hub", "Katanga / Haut-Katanga — Lubumbashi, Likasi, Kolwezi, Kipushi"),
            ("Corridor distance", "Katanga → Dar es Salaam ~2,000 km (multi-week journey)"),
            ("Top brands", "SINOTRUK HOWO leads in DRC mining; SHACMAN is gaining share"),
            ("Toll booths", "Six toll booths on 400 km Haut-Katanga route (industry complaint)"),
        ],
        "buyer_types": [
            ("Mining majors", "Kamoa Copper (Ivanhoe/Zijin), Glencore, China Moly — fleet contracts"),
            ("Artisanal miners", "Small-scale cobalt and copper miners"),
            ("Cross-border hauliers", "DRC-Tanzania, DRC-Zambia corridor operators"),
            ("Construction fleets", "Road, hydropower, urban development in Kinshasa, Lubumbashi"),
        ],
        "common_applications": "Copper and cobalt haulage from Katanga province, gold mining logistics in Ituri and South Kivu, cross-border supply routes via Tanzania and Zambia ports, road construction in remote provinces.",
        "shipping_days": "35–45 days",
        "import_notes": [
            "OFIDA (Office des Douanes et Accises) handles customs",
            "FERI (Foreign Exchange for Import) required since 2024",
            "Inter-regional corridors may require separate transit documents for Zambia, Tanzania",
        ],
        "recommended_trucks": [
            {"img": "shacman-x3000-6x4-mining.jpg", "type": "MINING DUMP", "name": "SHACMAN X3000 6×4 Mining Tipper", "desc": "Heavy-duty mining configuration for Katanga copper haulage. Reinforced chassis, tropical cooling.", "link": "products/x3000.html"},
            {"img": "shacman-f3000-6x4-highway.jpg", "type": "HEAVY DUMP", "name": "SHACMAN F3000 8×4 Mining Dump", "desc": "8×4 configuration for higher payload in Cobalt and Copper concentrate haulage.", "link": "products/f-series.html"},
            {"img": "shacman-x3000-6x4-tractor.jpg", "type": "TRACTOR HEAD", "name": "SHACMAN X3000 6×4 Tractor Head", "desc": "Katanga → Dar es Salaam 2,000 km long-haul. Reinforced cab suspension for corrugated roads.", "link": "products/x3000.html"},
        ],
        "faqs": [
            ("Is SHACMAN used in DRC mining?", "Yes — SHACMAN is gaining share in Katanga mining. SINOTRUK HOWO is the historical leader; SHACMAN offers competitive pricing for the same operating conditions."),
            ("What's the best truck for Katanga copper haulage?", "X3000 6×4 mining tipper or F3000 8×4 dump, depending on payload and road profile. We can recommend after reviewing your specific mine and route."),
            ("How do you handle OFIDA / FERI customs?", "We work with Kinshasa and Lubumbashi customs agents to manage OFIDA clearance and the new FERI requirement. CIF Matadi or CIF Dar es Salaam both available."),
        ],
    },
    {
        "slug": "uganda",
        "name": "Uganda",
        "flag": "🇺🇬",
        "hero_title": "SHACMAN Trucks for Uganda — Landlocked East Africa Hub",
        "hero_sub": "Tractor heads, dump trucks, and rigid chassis for Uganda's 26,000+ heavy-duty fleet. Cross-border container haulage from Mombasa and Dar es Salaam.",
        "port": "Mombasa (Kenya) / Dar es Salaam (Tanzania)",
        "port_detail": "Uganda is landlocked — all imports enter through Mombasa (most traffic) or Dar es Salaam. The Mombasa-Kampala corridor is the busiest in East Africa.",
        "market_data": [
            ("Truck fleet size", "26,000+ heavy-duty trucks (industry estimate 2024)"),
            ("Best-selling models", "6×4 tractor head, 6×4 rigid, 8×4 rigid"),
            ("Main highway", "Mombasa — Nairobi — Kampala (1,500 km), Dar — Kampala via Mutukula"),
            ("SHACMAN presence", "Active dealer network in Kampala; spare parts locally available"),
        ],
        "buyer_types": [
            ("Container hauliers", "Mombasa ↔ Kampala ↔ Juba (South Sudan) container freight"),
            ("Petroleum distributors", "Fuel distribution from Mombasa pipeline terminus and inland depots"),
            ("Agricultural traders", "Coffee, tea, maize, sugar transport"),
            ("Construction fleets", "Kampala-Entebbe expressway, urban development, oil & gas in Albertine region"),
        ],
        "common_applications": "Cross-border container haulage from Mombasa and Dar es Salaam ports, oil and petroleum distribution, agricultural produce collection, construction material transport.",
        "shipping_days": "25–35 days",
        "import_notes": [
            "EAC Certificate of Origin (Form E) — preferential tariff",
            "Uganda Revenue Authority (URA) ASYCUDA World system",
            "Pre-shipment inspection by Bureau Veritas or SGS for high-value imports",
        ],
        "recommended_trucks": [
            {"img": "shacman-x3000-6x4-tractor.jpg", "type": "TRACTOR HEAD", "name": "SHACMAN X3000 6×4 Tractor Head", "desc": "The top-selling model in Uganda — Mombasa-Kampala-Juba long-haul. Flagship cabin for driver comfort.", "link": "products/x3000.html"},
            {"img": "shacman-f3000-6x4-highway.jpg", "type": "DUMP TRUCK", "name": "SHACMAN F3000 6×4 Rigid Dump", "desc": "Standard for construction material, aggregate, and Albertine oil & gas logistics.", "link": "products/f-series.html"},
            {"img": "shacman-l3000-6x4-cargo.jpg", "type": "CARGO TRUCK", "name": "SHACMAN L3000 6×4 Cargo", "desc": "Agricultural produce and regional distribution within Uganda.", "link": "products/l3000.html"},
        ],
        "faqs": [
            ("What's the most popular SHACMAN truck in Uganda?", "X3000 6×4 tractor head — for Mombasa-Kampala-Juba long-haul. The F3000 6×4 and 8×4 rigid are close behind for construction and mining."),
            ("Where do SHACMAN trucks arrive in Uganda?", "Through Mombasa (Kenya) — about 80% of Uganda's imports — then overland to Kampala. We arrange shipping and inland logistics as part of the CIF package."),
            ("Is there SHACMAN dealer support in Uganda?", "Yes — SHACMAN has active dealers in Kampala with parts inventory. We coordinate with them for warranty and service support."),
        ],
    },
]

# Templates per country — same structure, different content
def render_country(c):
    # Build market data HTML
    market_rows = "".join(
        f'<div style="display:flex;align-items:flex-start;padding:10px 0;border-bottom:1px solid #e0e4e8"><div style="flex:0 0 220px;font-weight:700;color:#1a1a2e;font-size:14px">{k}</div><div style="flex:1;color:#555;font-size:14px">{v}</div></div>'
        for k, v in c["market_data"]
    )
    buyer_items = "".join(
        f'<div style="padding:16px;background:#f7f9fc;border-radius:8px;border-left:3px solid #c8102e"><h4 style="margin:0 0 6px;color:#1a1a2e;font-size:15px">{bt[0]}</h4><p style="margin:0;color:#666;font-size:13px;line-height:1.6">{bt[1]}</p></div>'
        for bt in c["buyer_types"]
    )
    truck_cards = "".join(
        f'''<div style="background:#fff;border-radius:10px;overflow:hidden;box-shadow:0 2px 12px rgba(0,0,0,0.08)">
                <img src="images/trucks/{t['img']}" alt="{t['name']}" style="width:100%;height:200px;object-fit:cover" loading="lazy">
                <div style="padding:20px">
                    <div style="font-size:12px;color:#c8102e;font-weight:700;letter-spacing:1.5px;margin-bottom:6px">{t['type']}</div>
                    <h3 style="margin:0 0 8px;font-size:18px">{t['name']}</h3>
                    <p style="color:#666;font-size:14px;margin:0 0 16px;line-height:1.6">{t['desc']}</p>
                    <a href="{t['link']}" style="color:#c8102e;text-decoration:none;font-weight:600;font-size:14px">View Details →</a>
                </div>
            </div>'''
        for t in c["recommended_trucks"]
    )
    import_items = "".join(f'<li style="margin-bottom:8px;color:#555;font-size:14px">{n}</li>' for n in c["import_notes"])
    faq_items = "".join(
        f'''<details style="background:#fff;border-radius:8px;padding:16px 20px;margin-bottom:10px;border-left:4px solid #c8102e;cursor:pointer">
            <summary style="font-weight:600;color:#1a1a2e;font-size:15px;cursor:pointer;list-style:none">{q}</summary>
            <p style="margin:12px 0 0;color:#555;line-height:1.7;font-size:14px">{a}</p>
        </details>'''
        for q, a in c["faqs"]
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{c['hero_title']} | YU Truck Export</title>
    <meta name="description" content="{c['hero_sub'][:155]}...">
    <meta name="keywords" content="SHACMAN {c['name']}, SHACMAN trucks {c['name']}, dump truck {c['name']}, tractor truck {c['name']}, heavy truck {c['name']}, SHACMAN export Africa, YU Truck Export">
    <link rel="canonical" href="https://yutruckexport.com/shacman-trucks-{c['slug']}.html">
    <link rel="alternate" hreflang="en" href="https://yutruckexport.com/shacman-trucks-{c['slug']}.html">
    <meta property="og:title" content="{c['hero_title']} | YU Truck Export">
    <meta property="og:description" content="{c['hero_sub'][:155]}...">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://yutruckexport.com/shacman-trucks-{c['slug']}.html">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap">
    <link rel="stylesheet" href="assets/css/style.css">
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ccircle cx='50' cy='50' r='45' fill='%23c8102e'/%3E%3Ctext x='50' y='62' font-size='50' font-weight='900' text-anchor='middle' fill='white' font-style='italic' font-family='sans-serif'%3ES%3C/text%3E%3C/svg%3E">
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "WebPage",
      "name": "{c['hero_title']}",
      "description": "{c['hero_sub'][:155]}",
      "url": "https://yutruckexport.com/shacman-trucks-{c['slug']}.html",
      "publisher": {{
        "@type": "Organization",
        "name": "YU Truck Export",
        "url": "https://yutruckexport.com/"
      }}
    }}
    </script>
</head>
<body>

<!-- HEADER -->
<header class="site-header">
    <div class="header-inner">
        <a href="index.html" class="logo">
            <span class="logo-mark">Y</span>
            <span>
                <span class="logo-text">YU TRUCK EXPORT</span><span class="logo-sub" style="display:block; font-size:11px; letter-spacing:1.5px; color:#666; margin-top:3px; font-weight:500;">SHACMAN</span>
            </span>
        </a>
        <nav class="main-nav">
            <ul>
                <li><a href="index.html">Home</a></li>
                <li><a href="products.html">Products</a></li>
                <li><a href="index.html#africa-markets" class="active">Africa</a></li>
                <li><a href="about.html">About</a></li>
                <li><a href="contact.html" class="header-cta">Get a Quote</a></li>
            </ul>
        </nav>
        <button class="nav-toggle" aria-label="Menu">☰</button>
    </div>
</header>

<!-- HERO -->
<section class="hero" style="min-height:540px">
    <img class="hero-img" src="images/trucks/hero-h3000.jpg" alt="{c['hero_title']}" loading="eager">
    <div class="hero-content">
        <span class="hero-tag">{c['flag']} {c['name']}</span>
        <h1>{c['hero_title']}</h1>
        <p class="hero-sub">{c['hero_sub']}</p>
        <div class="hero-actions">
            <a href="https://wa.me/8619992988805?text=Hi%20Yu%2C%20I%27m%20in%20{c['name']}%20and%20looking%20for%20SHACMAN%20trucks" class="btn btn-whatsapp" target="_blank" rel="noopener">💬 Chat with Yu</a>
            <a href="contact.html" class="btn btn-outline">Request a Quote</a>
        </div>
    </div>
</section>

<!-- MARKET SNAPSHOT -->
<section class="section">
    <div class="container">
        <div class="section-head">
            <span class="eyebrow">{c['name']} Market Snapshot</span>
            <h2>SHACMAN trucks for {c['name']}</h2>
            <p style="max-width:780px;margin:0 auto;font-size:17px">{c['port_detail']}</p>
        </div>

        <div style="background:#fff;border-radius:10px;box-shadow:0 2px 12px rgba(0,0,0,0.06);padding:24px 32px;margin-top:24px">
            {market_rows}
        </div>
    </div>
</section>

<!-- BUYER TYPES -->
<section class="section section-light" style="background:#f7f9fc">
    <div class="container">
        <div class="section-head">
            <span class="eyebrow">Typical Buyers in {c['name']}</span>
            <h2>Who buys SHACMAN in {c['name']}</h2>
            <p>Our {c['name']} customers include:</p>
        </div>

        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px;margin-top:24px">
            {buyer_items}
        </div>
    </div>
</section>

<!-- RECOMMENDED TRUCKS -->
<section class="section">
    <div class="container">
        <div class="section-head">
            <span class="eyebrow">Recommended Trucks</span>
            <h2>SHACMAN trucks for {c['name']}</h2>
            <p>Commonly requested configurations for {c['name']} customers. <strong>Shipping: {c['shipping_days']} from China.</strong></p>
        </div>

        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px;margin-top:32px">
            {truck_cards}
        </div>
    </div>
</section>

<!-- IMPORT NOTES -->
<section class="section section-light" style="background:#f7f9fc">
    <div class="container" style="max-width:900px">
        <div class="section-head">
            <span class="eyebrow">Import Notes for {c['name']}</span>
            <h2>What to know before importing</h2>
        </div>
        <ul style="list-style:none;padding:0;margin-top:24px;background:#fff;border-radius:10px;padding:24px 32px;box-shadow:0 2px 12px rgba(0,0,0,0.06)">
            {import_items}
        </ul>
    </div>
</section>

<!-- FAQ -->
<section class="section">
    <div class="container" style="max-width:900px">
        <div class="section-head">
            <span class="eyebrow">Frequently Asked Questions</span>
            <h2>Questions from {c['name']} buyers</h2>
        </div>
        <div style="margin-top:24px">
            {faq_items}
        </div>
    </div>
</section>

<!-- CTA -->
<section class="section" style="background:#1a1a2e;color:#fff;text-align:center">
    <div class="container">
        <div class="section-head">
            <span class="eyebrow" style="color:#c8102e">Get a Quote</span>
            <h2 style="color:#fff">Looking for SHACMAN trucks in {c['name']}?</h2>
            <p style="color:#ccc;max-width:680px;margin:0 auto">Send me the truck type, quantity and destination port ({c['port']}). I will check available options and reply on WhatsApp.</p>
        </div>
        <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap;margin-top:24px">
            <a href="https://wa.me/8619992988805?text=Hi%20Yu%2C%20I%27m%20in%20{c['name']}%20and%20looking%20for%20SHACMAN%20trucks" class="btn btn-whatsapp" target="_blank" rel="noopener">💬 Chat with Yu on WhatsApp</a>
            <a href="contact.html" class="btn btn-outline" style="border-color:#fff;color:#fff">Request a Quote</a>
        </div>
    </div>
</section>

<!-- FOOTER -->
<footer class="site-footer">
    <div class="container">
        <div class="footer-grid">
            <div>
                <div class="footer-brand">
                    <span class="logo-mark">Y</span>YU TRUCK EXPORT</div>
                <p class="footer-tagline">China heavy truck export supplier. SHACMAN trucks shipped from Chinese ports to {c['name']} and other African markets.</p>
            </div>
            <div class="footer-col">
                <h4>Products</h4>
                <ul>
                    <li><a href="products.html#dump">Dump Trucks</a></li>
                    <li><a href="products.html#tractor">Tractor Trucks</a></li>
                    <li><a href="products.html#cargo">Cargo Trucks</a></li>
                    <li><a href="products.html#special">Special Trucks</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Other Markets</h4>
                <ul>
                    <li><a href="shacman-trucks-tanzania.html">Tanzania</a></li>
                    <li><a href="shacman-trucks-zambia.html">Zambia</a></li>
                    <li><a href="shacman-trucks-kenya.html">Kenya</a></li>
                    <li><a href="shacman-trucks-cameroon.html">Cameroon</a></li>
                    <li><a href="shacman-trucks-ghana.html">Ghana</a></li>
                    <li><a href="shacman-trucks-nigeria.html">Nigeria</a></li>
                    <li><a href="shacman-trucks-drc.html">DR Congo</a></li>
                    <li><a href="shacman-trucks-uganda.html">Uganda</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Get in Touch</h4>
                <ul>
                    <li>💬 <a href="https://wa.me/8619992988805"><strong>+86 199 9298 8805</strong></a></li>
                    <li>✉️ <a href="mailto:weny47397@gmail.com">weny47397@gmail.com</a></li>
                    <li>📍 Xi'an, Shaanxi, China</li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            &copy; 2026 SHAAN XI HAN OCEAN CO., LTD | All Rights Reserved
        </div>
    </div>
</footer>

<a href="https://wa.me/8619992988805?text=Hi%20Yu%2C%20I%27m%20looking%20for%20SHACMAN%20trucks" class="whatsapp-float" target="_blank" rel="noopener" aria-label="Chat on WhatsApp"><span class="wa-icon">💬</span><span class="wa-label">Chat on WhatsApp</span></a>

<script src="assets/js/main.js"></script>
</body>
</html>
"""

for c in COUNTRIES:
    html = render_country(c)
    out = f"shacman-trucks-{c['slug']}.html"
    with open(out, "w") as f:
        f.write(html)
    print(f"✅ {out}  ({len(html):,} bytes)")
print(f"\nTotal: {len(COUNTRIES)} countries built.")