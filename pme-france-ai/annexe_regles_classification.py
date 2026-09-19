# -*- coding: utf-8 -*-
import re, json, unicodedata

def na(s):
    s=unicodedata.normalize('NFD', (s or '').lower())
    return ''.join(c for c in s if unicodedata.category(c)!='Mn')

# ordre = priorite (le premier qui matche gagne)
RULES = [
 ("Propreté / nettoyage / multiservices", r"nettoyage|proprete|entretien de locaux|multiservice|hygiene des locaux|blanchisserie industrielle|3d\b|deratisation|desinfection"),
 ("Sécurité / surveillance / télésurveillance", r"securite privee|gardiennage|surveillance|telesurveillance|alarme|videoprotection|surete"),
 ("Transport & logistique (commissionnaire, affrètement)", r"transport|affretement|commissionnaire|messagerie|logistique|fret|dechet.*collecte|coursier|demenagement|entreposage"),
 ("Courtage assurance / intermédiation financière", r"courtage|courtier|assurance|portefeuille d.assurance|mutuelle|credit|patrimoine|gestion de patrimoine"),
 ("Immobilier : agence, syndic, gestion locative", r"agence immobiliere|syndic|gestion locative|administrateur de biens|transaction immobiliere|immobilier d.entreprise"),
 ("Recrutement / intérim / RH / paie", r"recrutement|interim|travail temporaire|ressources humaines|relations humaines|chasse de tete|portage salarial|paie\b|gestion sociale|charges sociales"),
 ("Formation professionnelle / organisme de formation", r"organisme de formation|centre de formation|formation professionnelle|bilan de competences|e-learning|cfa\b|auto-ecole"),
 ("Services informatiques / ESN / éditeur de logiciel", r"informatique|logiciel|editeur|esn\b|ssii|infogerance|cyber|saas|numerique|web\b|digital|telecom|reseaux et systemes|hebergement"),
 ("Bureau d'études / ingénierie / diagnostics", r"bureau d.etude|ingenierie|ingenieur|etudes techniques|maitrise d.oeuvre|diagnostic|geometre|controle technique|expertise technique|r&d|essais|metrologie|acoustique|thermique|environnement.*etude"),
 ("Communication / marketing / édition / imprimerie / PLV", r"communication|marketing|publicit|imprimerie|edition|plv|signaletique|agence de com|evenementiel|audiovisuel|photograph|regie|media"),
 ("Conseil / expertise / services administratifs aux entreprises (BPO)", r"conseil|cabinet|audit|expertise comptable|comptab|juridique|avocat|traduction|secretariat|externalisation|bpo|centre d.appel|call center|relation client|recouvrement|domiciliation|assistance administrative|back-office|paie"),
 ("Négoce / distribution B2B", r"negoce|distribution|distributeur|grossiste|commerce de gros|fournitures|vente et installation|quincaillerie|approvisionnement|import|revendeur|emballage|consommables|materiel"),
 ("Services à la personne / santé à domicile", r"services a la personne|aide a domicile|garde d.enfant|maintien a domicile|portage de repas|creche|petite enfance|silver|ehpad|soins a domicile|materiel medical"),
 ("Santé / pharmacie / laboratoire / cabinet médical", r"pharmacie|officine|laboratoire d.analyse|ophtalmolog|dentaire|opticien|veterinaire|audioproth|kine|medical|clinique|psycholog"),
 ("HCR / restauration / tourisme / loisirs", r"restaurant|brasserie|pizzeria|bar\b|tabac|hotel|camping|traiteur|creperie|snack|boulangerie|patisserie|boucherie|charcuterie|cave\b|discotheque|agence de voyage|tourisme|loisir|sport|fitness|club\b|salle de|cinema"),
 ("Commerce de détail / e-commerce BtoC", r"magasin|boutique|commerce de detail|pret-a-porter|vente en ligne|e-commerce|marketplace|franchise.*commerce|supermarche|superette|fleuriste|bijouterie|librairie|jardinerie|animalerie|centre commercial"),
 ("Automobile / 2 roues / nautisme", r"garage|carrosserie|automobile|vehicule|concession|pneu|moto\b|nautisme|bateau|caravane|poids lourd"),
 ("Bâtiment / travaux publics / second œuvre", r"batiment|btp|maconnerie|menuiserie|charpente|couverture|plomberie|chauffage|climatisation|electricite|peinture|platrerie|isolation|etancheite|carrelage|serrurerie|metallerie|vitrerie|facade|terrassement|genie civil|travaux publics|renovation|piscine|paysag|espaces verts|agencement|pose de|installation electrique|second oeuvre|menuiseries|veranda|cloisons|sols|toiture|echafaudage|desamiantage|ascenseur|portail"),
 ("Industrie / production / fabrication", r"fabrication|usinage|fabricant|industrie|chaudronnerie|mecanique|plastique|injection|tolerie|decoupe|traitement de surface|fonderie|textile|imprim|moule|machines speciales|agroalimentaire|brasserie artisanale|cosmetique|chimie|production|manufactur|assemblage|electronique|menuiserie industrielle|scierie|bois"),
 ("Agriculture / viticulture / pêche", r"agricole|viticole|vignoble|domaine|exploitation agricole|elevage|horticole|peche|maraich"),
 ("Énergie / environnement / déchets / recyclage", r"photovoltaique|energie|solaire|recyclage|dechet|eau\b|assainissement|environnement"),
]
def classify(*texts):
    t=na(' '.join(x or '' for x in texts))
    for name,pat in RULES:
        if re.search(pat,t): return name
    return "Autres / non classé"

OFFICE = {
 "Propreté / nettoyage / multiservices",
 "Sécurité / surveillance / télésurveillance",
 "Transport & logistique (commissionnaire, affrètement)",
 "Courtage assurance / intermédiation financière",
 "Immobilier : agence, syndic, gestion locative",
 "Recrutement / intérim / RH / paie",
 "Formation professionnelle / organisme de formation",
 "Services informatiques / ESN / éditeur de logiciel",
 "Bureau d'études / ingénierie / diagnostics",
 "Communication / marketing / édition / imprimerie / PLV",
 "Conseil / expertise / services administratifs aux entreprises (BPO)",
 "Négoce / distribution B2B",
 "Services à la personne / santé à domicile",
}
