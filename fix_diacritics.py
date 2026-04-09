import os

replacements = [
    # Title-specific
    ('Zasady ochrany osobnich udaju', 'Zásady ochrany osobních údajů'),
    ('Zasady pouzivani cookies', 'Zásady používání cookies'),

    # Common date
    ('Posledni aktualizace: duben', 'Poslední aktualizace: duben'),

    # Privacy policy content
    ('Spravcem vasich osobnich udaju je spolecnost', 'Správcem vašich osobních údajů je společnost'),
    ('se sidlem Preslova 72/25, Praha 150 00, Ceska republika, IC: 14303388, DIC: CZ14303388', 'se sídlem Přeslova 72/25, Praha 150 00, Česká republika, IČ: 14303388, DIČ: CZ14303388'),
    ('Kontakt pro zalezitosti ochrany osobnich udaju:', 'Kontakt pro záležitosti ochrany osobních údajů:'),
    ('Jake osobni udaje shromazdujeme', 'Jaké osobní údaje shromažďujeme'),
    ('Prostrednictvim kontaktniho formulare na nasich webovych strankach muzeme shromazdovat nasledujici osobni udaje:', 'Prostřednictvím kontaktního formuláře na našich webových stránkách můžeme shromažďovat následující osobní údaje:'),
    ('Jmeno a prijmeni', 'Jméno a příjmení'),
    ('E-mailova adresa', 'E-mailová adresa'),
    ('Telefonni cislo', 'Telefonní číslo'),
    ('Nazev spolecnosti', 'Název společnosti'),
    ('Popis projektu a pozadavku', 'Popis projektu a požadavků'),
    ('Ucel zpracovani', 'Účel zpracování'),
    ('Vase osobni udaje zpracovavame za ucelem:', 'Vaše osobní údaje zpracováváme za účelem:'),
    ('Odpovedi na vase projektove poptavky a dotazy', 'Odpovědi na vaše projektové poptávky a dotazy'),
    ('Komunikace ohledne potencialni spoluprace', 'Komunikace ohledně potenciální spolupráce'),
    ('Pripravy nabidek a kalkulaci', 'Přípravy nabídek a kalkulací'),
    ('Pravnim zakladem zpracovani je nas opravneny zajem (cl. 6 odst. 1 pism. f) GDPR) spocivajici v odpovidani na obchodni poptavky a navazovani obchodnich vztahu.', 'Právním základem zpracování je náš oprávněný zájem (čl. 6 odst. 1 písm. f) GDPR) spočívající v odpovídání na obchodní poptávky a navazování obchodních vztahů.'),
    ('Prijemci osobnich udaju', 'Příjemci osobních údajů'),
    ('Vase osobni udaje mohou byt sdileny s nasledujicimi treti stranami, ktere nam pomahaji s provozem nasich webovych stranek:', 'Vaše osobní údaje mohou být sdíleny s následujícími třetí stranami, které nám pomáhají s provozem našich webových stránek:'),
    ('sluzba pro dorucovani e-mailu, ktera zpracovava data z kontaktniho formulare a odesilaje na nasi e-mailovou adresu', 'služba pro doručování e-mailů, která zpracovává data z kontaktního formuláře a odesílá je na naši e-mailovou adresu'),
    ('sluzba CDN a DNS, ktera zajistuje bezpecnost a rychlost naseho webu', 'služba CDN a DNS, která zajišťuje bezpečnost a rychlost našeho webu'),
    ('hostingova sluzba, na ktere jsou nase webove stranky provozovany', 'hostingová služba, na které jsou naše webové stránky provozovány'),
    ('Predavani udaju mimo EU', 'Předávání údajů mimo EU'),
    ('Nektere z nasich poskytovatelu sluzeb mohou zpracovavat udaje mimo Evropsky hospodarsky prostor:', 'Některé z našich poskytovatelů služeb mohou zpracovávat údaje mimo Evropský hospodářský prostor:'),
    ('Predavani udaju do USA je zajisteno na zaklade standardnich smluvnich dolozek (Standard Contractual Clauses) schvalenych Evropskou komisi, ktere zaruci odpovijajici uroven ochrany vasich osobnich udaju.', 'Předávání údajů do USA je zajištěno na základě standardních smluvních doložek (Standard Contractual Clauses) schválených Evropskou komisí, které zaručí odpovídající úroveň ochrany vašich osobních údajů.'),
    ('Doba uchovavani', 'Doba uchovávání'),
    ('Vase osobni udaje uchovavame po dobu', 'Vaše osobní údaje uchováváme po dobu'),
    ('od posledniho kontaktu, nebo do okamziku, kdy pozadate o jejich vymazani, podle toho, co nastane drive.', 'od posledního kontaktu, nebo do okamžiku, kdy požádáte o jejich vymazání, podle toho, co nastane dříve.'),
    ('Vase prava', 'Vaše práva'),
    ('V souvislosti se zpracovanim vasich osobnich udaju mate nasledujici prava:', 'V souvislosti se zpracováním vašich osobních údajů máte následující práva:'),
    ('Pravo na pristup', 'Právo na přístup'),
    ('muzete pozadat o informaci, zda a jake vase osobni udaje zpracovavame', 'můžete požádat o informaci, zda a jaké vaše osobní údaje zpracováváme'),
    ('Pravo na opravu', 'Právo na opravu'),
    ('muzete pozadat o opravu nepresnych nebo neuplnych udaju', 'můžete požádat o opravu nepřesných nebo neúplných údajů'),
    ('Pravo na vymazani', 'Právo na vymazání'),
    ('muzete pozadat o vymazani vasich osobnich udaju', 'můžete požádat o vymazání vašich osobních údajů'),
    ('Pravo na omezeni zpracovani', 'Právo na omezení zpracování'),
    ('muzete pozadat o omezeni zpracovani vasich udaju', 'můžete požádat o omezení zpracování vašich údajů'),
    ('Pravo na prenositelnost', 'Právo na přenositelnost'),
    ('muzete pozadat o predani vasich udaju jinemu spravci', 'můžete požádat o předání vašich údajů jinému správci'),
    ('Pravo vznest namitku', 'Právo vznést námitku'),
    ('muzete vznest namitku proti zpracovani zalozenemu na opravnenem zajmu', 'můžete vznést námitku proti zpracování založenému na oprávněném zájmu'),
    ('Pro uplatneni svych prav nas kontaktujte na:', 'Pro uplatnění svých práv nás kontaktujte na:'),
    ('Pravo podat stiznost', 'Právo podat stížnost'),
    ('Pokud se domnivate, ze zpracovani vasich osobnich udaju je v rozporu s pravnimi predpisy, mate pravo podat stiznost u dozoroveho uradu, kterym je:', 'Pokud se domníváte, že zpracování vašich osobních údajů je v rozporu s právními předpisy, máte právo podat stížnost u dozorového úřadu, kterým je:'),
    ('Urad pro ochranu osobnich udaju (UOOU)', 'Úřad pro ochranu osobních údajů (ÚOOÚ)'),
    ('Spravce osobnich udaju', 'Správce osobních údajů'),

    # Cookies-specific
    ('Cookies jsou male textove soubory, ktere se ukladaji do vaseho zarizeni (pocitace, tabletu, telefonu) pri navsteve webovych stranek. Pomahaji webovym strankam fungovat spravne a bezpecne.', 'Cookies jsou malé textové soubory, které se ukládají do vašeho zařízení (počítače, tabletu, telefonu) při návštěvě webových stránek. Pomáhají webovým stránkám fungovat správně a bezpečně.'),
    ('Jake cookies pouzivame', 'Jaké cookies používáme'),
    ('Nase webove stranky pouzivaji', 'Naše webové stránky používají'),
    ('pouze nezbytne technicke cookies', 'pouze nezbytné technické cookies'),
    ('ktere jsou nutne pro spravne fungovani webu. Nepouzivame zadne analyticke, marketingove ani reklamni cookies.', 'které jsou nutné pro správné fungování webu. Nepoužíváme žádné analytické, marketingové ani reklamní cookies.'),
    ('Konkretne se muze jednat o:', 'Konkrétně se může jednat o:'),
    ('Cookies pro zabezpeceni spojeni (SSL/TLS)', 'Cookies pro zabezpečení spojení (SSL/TLS)'),
    ('Cookies pro zachovani relace prohlizece', 'Cookies pro zachování relace prohlížeče'),
    ('Cookies tretich stran', 'Cookies třetích stran'),
    ('Nase webove stranky vyuzivaji sluzby tretich stran, ktere mohou do vaseho zarizeni ukladat vlastni cookies:', 'Naše webové stránky využívají služby třetích stran, které mohou do vašeho zařízení ukládat vlastní cookies:'),
    ('bezpecnostni cookies (napr.', 'bezpečnostní cookies (např.'),
    ('pro ochranu pred automatizovanymi utoky a zajisteni bezpecnosti naseho webu. Tyto cookies jsou nezbytne pro spravne fungovani bezpecnostnich funkci.', 'pro ochranu před automatizovanými útoky a zajištění bezpečnosti našeho webu. Tyto cookies jsou nezbytné pro správné fungování bezpečnostních funkcí.'),
    ('sluzby pro nacitani pisem mohou ukladat technicke cookies souvisejici s dorucovanim fontovych souboru a optimalizaci jejich nacitani.', 'služby pro načítání písem mohou ukládat technické cookies související s doručováním fontových souborů a optimalizací jejich načítání.'),
    ('Analyticke a marketingove cookies', 'Analytické a marketingové cookies'),
    ('Na nasich webovych strankach', 'Na našich webových stránkách'),
    ('nepouzivame Google Analytics ani zadne jine nastroje pro sledovani navstevnosti', 'nepoužíváme Google Analytics ani žádné jiné nástroje pro sledování návštěvnosti'),
    ('Nepouzivame zadne marketingove ci reklamni cookies a vasi aktivitu na webu nijak nesledujeme.', 'Nepoužíváme žádné marketingové či reklamní cookies a vaši aktivitu na webu nijak nesledujeme.'),
    ('Cookies muzete spravovat v nastaveni vaseho weboveho prohlizece. Vetsinau prohlizecu vam umoznuje:', 'Cookies můžete spravovat v nastavení vašeho webového prohlížeče. Většinou prohlížečů vám umožňuje:'),
    ('Zobrazit aktualne ulozene cookies', 'Zobrazit aktuálně uložené cookies'),
    ('Smazat vsechny nebo vybrane cookies', 'Smazat všechny nebo vybrané cookies'),
    ('Blokovat cookies ze vsech nebo vybranych webovych stranek', 'Blokovat cookies ze všech nebo vybraných webových stránek'),
    ('Nastavit upozorneni pred ulozenim cookies', 'Nastavit upozornění před uložením cookies'),
    ('Navody pro spravu cookies v nejbeznejsich prohlizecich:', 'Návody pro správu cookies v nejběžnějších prohlížečích:'),
    ('Nastaveni &gt; Soukromi a zabezpeceni &gt; Cookies a dalsi data webu', 'Nastavení &gt; Soukromí a zabezpečení &gt; Cookies a další data webu'),
    ('Nastaveni &gt; Soukromi a zabezpeceni &gt; Cookies a data stranek', 'Nastavení &gt; Soukromí a zabezpečení &gt; Cookies a data stránek'),
    ('Predvolby &gt; Soukromi &gt; Spravovat data webovych stranek', 'Předvolby &gt; Soukromí &gt; Spravovat data webových stránek'),
    ('Nastaveni &gt; Cookies a opravneni webu &gt; Spravovat a mazat cookies', 'Nastavení &gt; Cookies a oprávnění webu &gt; Spravovat a mazat cookies'),
    ('Upozornujeme, ze blokovani nezbytnych cookies muze ovlivnit funkcnost naseho webu.', 'Upozorňujeme, že blokování nezbytných cookies může ovlivnit funkčnost našeho webu.'),
    ('Pokud mate dotazy ohledne pouzivani cookies na nasich webovych strankach, kontaktujte nas na:', 'Pokud máte dotazy ohledně používání cookies na našich webových stránkách, kontaktujte nás na:'),

    # Navbar items
    ('>Uvod<', '>Úvod<'),
    ('>Sluzby<', '>Služby<'),
    ('>O nas<', '>O nás<'),
    ('mobile-menu-link">Uvod ', 'mobile-menu-link">Úvod '),
    ('mobile-menu-link">Sluzby ', 'mobile-menu-link">Služby '),
    ('mobile-menu-link">O nas ', 'mobile-menu-link">O nás '),

    # Footer nav
    ('>Poptavka<', '>Poptávka<'),
    ('>Vyvoj<', '>Vývoj<'),
    ('>Vyroba<', '>Výroba<'),
    ('>Prototypovani<', '>Prototypování<'),
    ('>Dodavky<', '>Dodávky<'),
    ('>Tym<', '>Tým<'),
    ('>O firme<', '>O firmě<'),

    # Footer legal
    ('Ochrana soukromi', 'Ochrana soukromí'),
    ('>Pristupnost<', '>Přístupnost<'),
    ('Vsechna prava vyhrazena', 'Všechna práva vyhrazena'),

    # Aria labels
    ('aria-label="Zpet nahoru"', 'aria-label="Zpět nahoru"'),
    ('aria-label="Zavrit"', 'aria-label="Zavřít"'),
]

script_dir = os.path.dirname(os.path.abspath(__file__))

for filename in ['privacy-policy.html', 'cookies.html']:
    filepath = os.path.join(script_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    count = 0
    for old, new in replacements:
        if old in content:
            n = content.count(old)
            content = content.replace(old, new)
            count += n
            print(f"  {filename}: replaced '{old[:50]}...' x{n}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n{filename}: {count} total replacements\n")

print("Done!")
