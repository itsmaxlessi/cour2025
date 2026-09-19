# Рынок продаваемых PME во Франции → отрасли под AI-автоматизацию → компании для контакта

**Дата сбора данных: 19 сентября 2026.** Все цифры сопровождаются URL. «Оценка» = мой вывод, а не данные источника.
**Ни с кем не связывался, нигде не регистрировался, ничего не оплачивал.** Все данные — из открытого доступа.

Файлы: `listings.csv` · `listings_all_raw.csv` · `sectors.md` · `prospects_negoce-b2b.csv` · `prospects_proprete.csv` · `annexe_stats_secteurs.txt` · `annexe_regles_classification.py`

---

## 1. Резюме на одну страницу

**Что продаётся.** Собрано **1 996 объявлений с 4 площадок** (Transentreprise 403, Fusacq 544, CRA 376, Bpifrance 673); после склейки дублей — **1 603 уникальных**. Структура рынка резко смещена от офисных бизнесов: **BTP (421), HCR/ресторация (368), промышленность (155), автосервис (61) и розница (26) = 64 %** уникальных объявлений. Весь офисно-сервисный периметр — **400 объявлений (25 %)**. Это совпадает с официальной статистикой: в 2024 г. HCR = 29 % цессий, commerce = 28 %, services aux entreprises = 16 % ([DGE, Théma n°30, juin 2025](https://www.entreprises.gouv.fr/files/files/Publications/2025/Th%C3%A9mas/thema-30-transmission.pdf)).
Мотив продажи там, где он раскрыт (226 объявлений CRA): **79 % — départ à la retraite**.

**Две выбранные отрасли.**

1. **Négoce / distribution B2B (commerce de gros interentreprises).** Крупнейший офисно-сервисный сегмент предложения — **104 уникальных объявления**, CA медиана 2 250 000 €, prix demandé медиана 950 000 €, p/CA = 0,51. Владение **не требует ни диплома, ни карты, ни членства в ордене** (проверено по репертуару регулируемых профессий Service-Public). Офисный труд — **оценка: 50–70 % штата** в PME с CA 2–5 M€. LLM не может заменить сам сервис (запас, логистика, торговый кредит).
2. **Propreté / nettoyage / facility multiservices.** 23 уникальных объявления (IdF 5, PACA 7), CA медиана 1 100 000 €, prix медиана 550 000 €, p/CA = 0,61. **Нулевой барьер для владения.** Услуга физическая → структурно защищена от обесценивания AI. Рынок гигантский и раздробленный: > 600 000 рабочих мест, > 18 млрд €, топ-50 держат лишь ~42 % ([FEP](https://www.federation-proprete.com/chiffres-cles-secteur-hygiene-proprete/)) — то есть **огромная база целей для «автоматизация как услуга»**.

**Почему не транспорт (сильный №3):** 75 объявлений и 5/5 по автоматизации, но attestation de capacité de commissionnaire обязан держать человек, обеспечивающий «direction permanente et effective» (décret n°90-200, art. 3) — при уходе продавца деятельность блокируется; плюс в IdF+PACA всего 6 объявлений из 75.
**Почему не ESN и не communication:** проходят по предложению и барьерам, но это ровно те услуги, стоимость которых снижают LLM.

**Важная поправка к вашим параметрам (факт, из реестра).** Сочетание «CA 1–5 M€ **и** 10–50 сотрудников» внутренне противоречиво для оптовой торговли: среди 2 275 собранных компаний négoce в IdF/PACA с 10–49 сотрудниками **медианный CA = 13,7 M€**, и только **13 %** попадают в 1–5 M€. В propreté наоборот: при 10–49 сотрудниках медиана CA = 730 k€, в диапазон 1–5 M€ попадают 28 %. Практический вывод: **в négoce ваш ценовой сегмент — это 3–15 человек, в propreté — 20–80 человек.** Поэтому в `prospects_negoce-b2b.csv` я намеренно расширил выборку на компании с 3–49 сотрудниками, чтобы сохранить главный критерий — CA 1–5 M€.

**Топ-10 компаний для первого контакта** (все — Île-de-France, CA в целевом диапазоне, независимые, директор 55+, старше 10 лет; полные данные и ещё 169 компаний — в двух `prospects_*.csv`):

| # | Компания | SIREN | NAF | Город | CA (год) | Résultat | Effectif | Дир. (возраст) | Отрасль |
|---|---|---|---|---|---|---|---|---|---|
| 1 | G.E.N IMPECCABLE | 479685638 | 81.21Z | Clichy-sous-Bois (93) | 3 353 758 € (2024) | +51 638 € | 20–49 | 61 | Propreté |
| 2 | HYGIENE HABITAT (2H) | 350969226 | 81.29A | La Garenne-Colombes (92) | 2 621 813 € (2024) | +327 184 € | 20–49 | 62 | Propreté |
| 3 | ESPACE NET | 431816628 | 81.21Z | Paris (75) | 1 805 133 € (2025) | +299 889 € | 20–49 | 73 | Propreté |
| 4 | M.N.A. | 444317739 | 81.21Z | Neuilly-sur-Seine (92) | 1 408 789 € (2024) | +77 940 € | 20–49 | 62 | Propreté |
| 5 | NETTOYAGE INDUSTRIEL ET MAINTENANCE (NIM) | 395007180 | 81.21Z | Boulogne-Billancourt (92) | 1 281 047 € (2024) | +6 662 € | 20–49 | 61 | Propreté |
| 6 | PROTECT SECURITE | 394995773 | 46.69B | Nanterre (92) | 4 106 501 € (2025) | +1 302 324 € | 20–49 | 60 | Négoce B2B |
| 7 | EXCILONE | 504565888 | 46.51Z | Élancourt (78) | 3 747 184 € (2025) | +305 054 € | 20–49 | 61 | Négoce B2B |
| 8 | BRUSER | 392502126 | 46.69B | Gargenville (78) | 2 688 193 € (2021) | +397 561 € | 20–49 | 59 | Négoce B2B |
| 9 | LCS | 402136071 | 46.51Z | Ennery (95) | 2 319 690 € (2024) | +11 572 € | 10–19 | 65 | Négoce B2B |
| 10 | RSW.NET | 398811323 | 46.18Z | Groslay (95) | 2 046 140 € (2022) | +116 921 € | 10–19 | 61 | Négoce B2B |

Источник по каждой строке: `https://annuaire-entreprises.data.gouv.fr/entreprise/<SIREN>` (данные RNE/INSEE через [recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr)).
Исключён из топ-10 **ASIATIDES IMPORT** (321 817 900), формально подходящий по размеру: résultat net −4 303 545 € за 2020 — слишком высокий риск для первого кейса.

**Первый платный пилот (рекомендация).** В **propreté** — цикл ежемесячной фактурации + relance impayés (самый измеримый и наименее рискованный). В **négoce** — разбор входящих заказов из email → черновик заказа в ERP + ARC клиенту. Детали, расчёты экономии и черновики писем — в разделе 5.

---

## 2. Этап 1 — скан объявлений о продаже

### 2.1 Что и как собрано (факт)

| Площадка | Доступ | Фильтр при сборе | Собрано | Итоговый файл |
|---|---|---|---|---|
| [Transentreprise](https://www.transentreprise.com/offres) (сеть CCI/CMA) | открыт | effectif 10–50, вся Франция, все отрасли | 403 | `listings_all_raw.csv` |
| [Fusacq](https://www.fusacq.com/reprendre-une-entreprise/resultats-annonces-cession-entreprise_fr_?ca=1000000;5000000&ca_null=0&nb_personnes=10;50) | открыт | CA 1–5 M€ + effectif 10–50 | 544 | — |
| [CRA](https://www.cra.asso.fr/liste-entreprises-a-reprendre.aspx) | открыт (публичный список) | без фильтра | 376 | — |
| [Bpifrance «Bourse de la transmission»](https://reprise-entreprise.bpifrance.fr/recherche?employeesCount=10;50&turnover=1000;5000) | открыт | CA 1–5 M€ + effectif 10–50 | 673 | — |
| **Итого** | | | **1 996 строк / 1 603 уникальных** | |

Критерий готовности «≥80 объявлений минимум с 3 площадок» перевыполнен в 20 раз: **509 объявлений в офисно-сервисном периметре** (`listings.csv`), **1 996 всего** (`listings_all_raw.csv`), 4 площадки.

Bpifrance — агрегатор объявлений CessionPME, Place des Commerces, Fusacq, Transentreprise и CRA. 393 строки помечены `doublon_probable` (совпадение первых 6 слов описания + CA) и исключены из медиан.

### 2.2 Структура полей `listings.csv`

`source | url | ref | date | activite | secteur | naf | region | ca | ebe | effectif | prix | raison | dependance | doublon_probable | notes`

Заполняемость (факт, по 1 603 уникальным): `ca` — 1 220 строк, `prix` — 828, `region` — 1 268, `naf` — 118 (только CRA публикует код NAF), `ebe` — 101 (только Bpifrance), `raison` — 226 (CRA + часть Transentreprise). Пустые поля оставлены пустыми, ничего не достраивал.

**Метод классификации по отраслям и его точность.** Колонка `secteur` — моя категория, присвоенная по ключевым словам в описании объявления (и в коде NAF там, где CRA его публикует), по правилам, приложенным целиком в `annexe_regles_classification.py`. Правила применяются по приоритету: первая сработавшая категория выигрывает. **Это даёт ошибки на пограничных случаях** — например, объявление «Distribution Produits "Bien-Etre"» (CRA N°18824) попало в «Négoce B2B» по слову *distribution*, хотя его код NAF — 47 (розница). Оценка доли таких ошибок: **5–10 %** в пределах офисного периметра. Для отраслевых медиан это не критично (выборки 20–100 объявлений), но **перед работой с конкретной строкой откройте её URL и проверьте.**

`dependance` (зависимость от владельца) остался пустым почти везде: **ни одна из четырёх площадок не публикует это поле в открытом доступе.** В `notes` по объявлениям CRA и Transentreprise сохранён текст описания — там зависимость иногда читается косвенно («accompagnement du cédant possible», «équipe en place autonome»).

### 2.3 Что не удалось получить

- **Cessionpme.com** — HTTP 403 на любые автоматические запросы (и через WebFetch, и через curl). Его объявления частично покрыты через агрегатор Bpifrance (поле `notes` содержит источник-партнёра).
- **Полные досье CRA** (effectif, EBE, детальная финансовая справка) — только для членов ассоциации. Публично доступны: activité, région, CA, valeur demandée, **код NAF** и **motif de cession** — я собрал их по 118 карточкам офисно-сервисного периметра.
- **Fusacq: цена и штат по конкретному объявлению** — видны только в карточке после входа в аккаунт. В списке доступны activité, CA, регион, референс, дата. Поэтому у 542 строк Fusacq поле `prix` пустое.
- **Мультипликатор prix/EBITDA** — практически нерасчётен: EBE публикует только Bpifrance и только в 101 объявлении из 1 603. Вместо него в `sectors.md` использован **p/CA** (prix demandé / CA), доступный по 828 объявлениям.
- **Pappers.fr** — HTTP 403. Заменён на официальный API [recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr) (те же данные RNE/INSEE: SIREN, NAF, effectif, CA, résultat, дирижанты с годом рождения).

---

## 3. Этап 2 — анализ отраслей

Полный разбор 10+ отраслей по всем 5 пунктам брифа (предложение, потенциал автоматизации, регуляторные барьеры по первичным источникам, риски, рыночный контекст) — в **`sectors.md`**. Здесь — только итоги.

### Отрасли с ≥5 объявлениями в офисно-сервисном периметре (факт)

| Отрасль | n уник. | IdF | PACA | CA медиана | Prix медиана | p/CA | Барьер для владения |
|---|---:|---:|---:|---:|---:|---:|---|
| Négoce / distribution B2B | 104 | 9 | 9 | 2 250 000 € | 950 000 € | 0,51 | **нет** |
| Transport & logistique | 75 | 4 | 2 | 2 200 488 € | 600 000 € | 0,43 | средний (attestation commissionnaire) |
| Services informatiques / ESN | 51 | 16 | 5 | 1 550 000 € | 665 000 € | 0,56 | нет |
| Communication / marketing / PLV | 51 | 11 | 3 | 2 000 000 € | 480 000 € | 0,43 | нет |
| Bureau d'études / ingénierie | 32 | 2 | 0 | 1 500 000 € | 750 000 € | 0,71 | низкий (сертификация операторов) |
| Services à la personne | 25 | 3 | 0 | 1 125 000 € | 217 500 € | 0,40 | средний (agrément / autorisation) |
| Propreté / nettoyage | 23 | 5 | 7 | 1 100 000 € | 550 000 € | 0,61 | **нет** |
| Conseil / BPO | 13 | 4 | 1 | 1 400 000 € | 550 000 € | 0,45 | нет (кроме expertise comptable) |
| Formation professionnelle | 10 | 3 | 1 | 1 135 000 € | 620 000 € | 0,50 | низкий (NDA + Qualiopi на компанию) |
| Recrutement / intérim | 7 | 4 | 0 | 1 471 608 € | 900 000 € | 0,87 | высокий для intérim (garantie 151 445 €) |
| Courtage assurance | 6 | 1 | 0 | 1 125 000 € | 512 500 € | 0,92 | **высокий** (ORIAS, capacité niveau I) |

### Регуляторные барьеры — проверено по первичным источникам

| Отрасль | Требование к **владельцу** | Первичный источник |
|---|---|---|
| **Négoce B2B** | нет. Регулируются отдельные **товары** (медикаменты, алкоголь, фитосанитарные, оружие, пищевой agrément), не профессия | [Répertoire des activités réglementées, Service-Public Entreprendre](https://entreprendre.service-public.gouv.fr/vosdroits/R60131) · [F35897](https://entreprendre.service-public.gouv.fr/vosdroits/F35897) |
| **Propreté** | нет. Рамка — конвенция IDCC 3043 (перенос персонала, annexe VII), трудовая, не разрешительная. Certibiocide нужен операторам 3D (NAF 8129A) | те же + [FEP](https://www.federation-proprete.com/chiffres-cles-secteur-hygiene-proprete/) |
| Transport / commissionnaire | attestation de capacité у лица с «direction permanente et effective»; capitaux propres ≥ **22 800 €**; аттестат по диплому, экзамену или 5 годам управленческого опыта за 10 лет | [Décret n°90-200, art. 2, 3, 4, 6, 7](https://www.legifrance.gouv.fr/loda/id/LEGITEXT000006075505) · [Ministère de la Transition écologique](https://www.ecologie.gouv.fr/politiques-publiques/commissionnaires-transport-routier) |
| Immobilier / syndic | **carte professionnelle**; аптитюд у **законного представителя** (bac+3 юр./экон./коммерч., BTS professions immobilières, либо 3 года опыта с bac / 10 лет без); garantie financière 30 000 € → 110 000 €; RCP | [Loi n°70-9 (Hoguet)](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000512228) · [Décret n°72-678](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000855024) · [Service-Public F38657](https://entreprendre.service-public.gouv.fr/vosdroits/F38657) |
| Courtage assurance | immatriculation ORIAS; **capacité professionnelle niveau I-IAS у руководителей**; RC pro; garantie financière при инкассации; членство в agréée association | [ORIAS](https://www.orias.fr/) · [FAQ ORIAS (PDF)](https://www.orias.fr/assets/ORIAS_FAQ.pdf) |
| Services à la personne | déclaration — свободно; **agrément** (5 лет, téléservice NOVA) обязателен для publics fragiles; autorisation département для SAD | [Service-Public F23633](https://entreprendre.service-public.gouv.fr/vosdroits/F23633) · [servicesalapersonne.gouv.fr](https://www.servicesalapersonne.gouv.fr/espace-pro/obligations-reglementaires/declaration-agrement-autorisation-dans-quel-cas) |
| Formation professionnelle | déclaration d'activité (NDA) + BPF; **Qualiopi** — для доступа к публичному финансированию (сертификация компании, не диплом владельца) | [travail-emploi.gouv.fr / Qualiopi](https://travail-emploi.gouv.fr/qualiopi-marque-de-certification-qualite-des-prestataires-de-formation) · [Service-Public F19087](https://entreprendre.service-public.gouv.fr/vosdroits/F19087) |
| Intérim (travail temporaire) | déclaration инспектору труда + **garantie financière ≥ 8 % CA и не ниже 151 445 € в 2026** | [Décret n°2025-1350 du 26 décembre 2025](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053176931) · art. L1251-49/L1251-50 Code du travail |

### Рейтинг и выбор топ-2

Критерий: **много продаётся × высокий потенциал автоматизации × нет барьера для владения × услуга не умирает от AI**. Оценки 1–5 — мои (**оценка**), итог = произведение (макс. 625). Полная таблица и обоснование каждой оценки — в `sectors.md`, §3.

| Место | Отрасль | n (факт) | Предл. | Автомат. | Нет барьера | Устойч. к AI | Итог |
|---|---|---:|---:|---:|---:|---:|---:|
| **1** | **Négoce / distribution B2B** | 104 | 5,0 | 5,0 | 5,0 | 5,0 | **625** |
| **2** | **Propreté / nettoyage / facility** | 23 | 3,0 | 4,0 | 5,0 | 5,0 | **300** |
| 3 | Transport & logistique | 75 | 4,5 | 5,0 | 2,5 | 5,0 | 281 |
| 4 | Bureau d'études / ingénierie | 32 | 3,5 | 4,5 | 4,0 | 3,0 | 189 |
| 5 | Services à la personne | 25 | 3,0 | 4,0 | 2,5 | 5,0 | 150 |
| 6–7 | Communication / PLV · ESN | 51 · 51 | 3,5 · 4,0 | 4,0 · 3,5 | 5,0 · 5,0 | 2,0 · 2,0 | 140 · 140 |

**Négoce B2B** выигрывает по всем четырём осям сразу. **Propreté** выбрана вторым, обгоняя транспорт (281) и ESN (140), потому что единственная из крупных альтернатив сочетает нулевой барьер владения с услугой, которую AI не обесценивает. Разрыв между 2-м и 3-м местом невелик (300 против 281) — **если вы готовы сдать экзамен на attestation de capacité de commissionnaire, транспорт объективно даёт больше целей (75 против 23) и столько же рутины.**

### Рыночный контекст (факт)

- **Объём рынка передач.** 37 200 цессий в 2024 г. (стабильно с 2022 после спада 2020). 86 % переданных компаний имели < 10 сотрудников в 2023 г.; доля компаний с ≥10 сотрудниками выросла с 10 % (2012) до 14 % (2023). Средняя цена цессии 303 000 €, медианная 125 000 €. Топ-10 % дороже 500 000 €. ([DGE, Théma n°30](https://www.entreprises.gouv.fr/files/files/Publications/2025/Th%C3%A9mas/thema-30-transmission.pdf))
- **Демография.** ~500 000 руководителей 60+ в 2022 г., 3 млн наёмных сотрудников. 33 % цессий инициируют руководители 60+ (пик — 61 год). Больше всего 60+ в enseignement/santé/action sociale (24 %), commerce (22 %), **services aux entreprises (18 %)**. (там же)
- **Сделки 1–50 M€.** 1 076 операций в 2025 против 1 226 в 2024 (−12 %). **Île-de-France = 38 % smallcap-рынка, −8 %; PACA −40 %** (худшая динамика). По секторам: TMT **+21 %** (единственный рост), services −47 %, distribution −39 %. Покупатели: некотируемые компании 68 %, фонды 20 %, французские покупатели 91 %. Build-up ≈ 50 % сделок. ([In Extenso Finance × Epsilon Research, «Régions & Transmission», 10-е изд.](https://finance.inextenso.fr/actualites/regions-transmission-10eme-edition-cessions-acquisitions-de-pme-2025-porte-par-le-build-up-le-marche-resiste-au-choc-dincertitude/))
- **Мультипликаторы.** Argos Index Q1 2026: 8,6x EBITDA, фонды 10,0x, стратеги 7,8x — **но это mid-market с equity value 15–500 M€**, к сегменту 1–5 M€ CA неприменимо напрямую ([Argos](https://argos.fund/mid-market-argos-index-for-the-first-quarter-of-2026/)). **Оценка:** для PME вашего размера реалистичный диапазон 3–5x EBE; наблюдаемый p/CA ≈ 0,5 при EBE 10–15 % CA даёт примерно то же.
- **Конъюнктура опта.** Продажи в commerce de gros: −0,3 % в объёме в 2025 после −1,3 % в 2024; наёмная занятость −1,4 % ([Insee, «Le compte du commerce en 2025»](https://www.insee.fr/fr/statistiques/9008999)).
- **Пропреté.** > 600 000 рабочих мест, > 18 млрд € оборота, ~14–16 тыс. компаний; топ-50 = 7,4 млрд € (≈42 %) ([FEP](https://www.federation-proprete.com/chiffres-cles-secteur-hygiene-proprete/)).

---

## 4. Этап 3 — компании для контакта

### 4.1 Источник и метод

Реестровые данные взяты из официального API **[recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr)** (данные INSEE Sirene + RNE, тот же источник, что и annuaire-entreprises.data.gouv.fr). Собрано **1 724 уникальные карточки** по négoce и **575** по propreté в IdF + PACA.

**Коды NAF, которые я использовал:**

- **Négoce / distribution B2B:** 46.69B, 46.69C, 46.74A, 46.74B, 46.73A, 46.76Z, 46.75Z, 46.52Z, 46.51Z, 46.66Z, 46.90Z, 46.49Z, 46.44Z, 46.43Z, 46.47Z, 46.71Z, 46.72Z, 46.18Z (оптовая торговля непищевая, технический и межпромышленный B2B).
- **Propreté / facility:** 81.21Z, 81.22Z, 81.29A, 81.29B, 81.10Z.

**Фильтры отбора:** активная компания; штаб-квартира в IdF (75, 77, 78, 91, 92, 93, 94, 95) или PACA (04, 05, 06, 13, 83, 84); возраст ≥ 10 лет; CA (если раскрыт) в коридоре 0,8–6 M€; ≤ 4 открытых учреждения (прокси независимости); есть идентифицируемый дирижант-физлицо (коммиссары по счетам исключены).

**Приоритет A/B/C** — по баллам: +3 за директора 55+, +1 за 60+, +2 за CA 1–5 M€, +1 за IdF, +1 за возраст компании ≥20 лет, +1 за штат 20–49. **A** = ≥6 баллов **и** директор 55+; **B** = 4–5; **C** = ≤3.

### 4.2 Результат

| Файл | Компаний | Приоритет A | Île-de-France | PACA |
|---|---:|---:|---:|---:|
| `prospects_negoce-b2b.csv` | **68** | 37 | 47 | 21 |
| `prospects_proprete.csv` | **111** | 52 | 102 | 9 |

Критерий «≥30 компаний на отрасль, у каждой SIREN и приоритет» выполнен.

### 4.3 Признаки низкой цифровизации — что удалось и что нет

**Что сделано (факт).** Для верхних строк каждого списка (все 68 в négoce, первые 70 из 111 в propreté) я автоматически проверил вероятный сайт компании (подбор домена от названия + проверка, что страница действительно про эту компанию) и просканировал главную на маркеры: espace client / extranet, devis или commande en ligne, форма контакта, отображаемый факс, наличие `viewport` (адаптивность).
Результат: **в négoce сайт найден у 32 из 68 проверенных, в propreté — у 19 из 70.** Колонка `site_web_probable` помечена как *probable* — метод даёт ложные срабатывания на общих доменах (`applications.fr`, `stephane.fr`), домен-совпадения с сайтами мэрий я отфильтровал.

**Чего сделать не удалось, честно:**
- **Вакансии на админ-роли по каждой компании** — `n/d`. Indeed отдаёт HTTP 403, Welcome to the Jungle — HTTP 202 (анти-бот), API France Travail требует партнёрского ключа. Публичный сайт France Travail доступен, но поиск по названию работодателя ненадёжен: значительная часть объявлений публикуется кадровыми агентствами без имени клиента.
  *Что вместо этого (факт, France Travail, 19.09.2026):* **«assistant administratif» — 582 предложения в Париже (75)**; по всей Франции: **«assistant administration des ventes» — 1 108**, **«gestionnaire ADV» — 823**, **«assistant facturation» — 180**, **«responsable exploitation propreté» — 73**. Отраслевой сигнал сильный; по каждой компании его нужно проверять вручную.
  Ссылка для ручной проверки: `https://candidat.francetravail.fr/offres/recherche?motsCles=<название компании>`
- **LinkedIn компании** — `n/d`. LinkedIn закрыт для автоматического доступа без входа в аккаунт, а регистрироваться бриф запрещает. Ручная проверка: `linkedin.com/company/` + название.
- **Общий email** — заполнен только там, где он был опубликован на найденной главной странице (email извлечён из публичной страницы компании; личные адреса и телефоны не собирал).
- **Независимость от группы** — приближена через число открытых учреждений (≤4). Это несовершенный прокси: например, FIDUCIAL OFFICE STORES прошёл фильтр, хотя входит в группу Fiducial. Перед контактом проверяйте акционеров в RNE.

### 4.4 Рекомендуемый порядок контакта

**Оценка.** Начинать с propreté: там 52 компании приоритета A против 37 в négoce, все в IdF, и у 51 из 70 проверенных **не нашлось сайта** — это самый сильный доступный сигнал слабой цифровизации. Négoce даёт более крупный и рентабельный актив (PROTECT SECURITE: résultat net 1,3 M€ при CA 4,1 M€), но и более подготовленного собеседника.

---

## 5. Этап 4 — заготовка предложения

> Все цифры экономии в этом разделе — **оценка**. Логика расчёта: загруженная стоимость часа офисного сотрудника принята **28 €/ч для assistant(e)/ADV и 32–35 €/ч для responsable** (валовая зарплата 30–40 k€ + ~45 % взносов, 1 600 оплачиваемых рабочих часов в год); рабочий год — 45 недель. Доля времени по процессам взята по типовой структуре PME соответствующего размера; **перед коммерческим предложением её обязательно измерять на месте** — это и есть содержание бесплатного разбора.

---

### 5.1 Négoce / distribution B2B

**Модельная компания:** CA 3 M€, 12 сотрудников, из них 7 в офисе (3 ADV, 1 achats, 1 compta, 1 responsable, 1 direction). EBE **оценка** 10 % CA = 300 000 €.

| # | Процесс | Как устроено сейчас | Что делает агент | Экономия (**оценка**) |
|---|---|---|---|---|
| 1 | **Приём и ввод заказов** (email, PDF, Excel, иногда факс) | 3 ADV × ~8 ч/нед вручную перепечатывают заявки в ERP | Разбирает вложение → структурированные строки заказа с кодом товара, количеством, ценой; отдаёт на подтверждение одним кликом | −60 % времени: 14,4 ч/нед → **≈ 18 100 €/год** |
| 2 | **Подготовка devis** | 2 чел. × 6 ч/нед: поиск цены, наличия, срока, условий по истории клиента | Черновик devis из прайса + истории клиента + сроков поставщика; человек проверяет и отправляет | −50 %: 6 ч/нед → **≈ 8 100 €/год** |
| 3 | **Сверка ARC поставщиков и отслеживание сроков** | 1 чел. × 6 ч/нед: сверка подтверждений с заказом, ловля расхождений по цене и дате | Автосверка ARC с заказом, выделение расхождений, авто-запрос поставщику при задержке | −70 %: 4,2 ч/нед → **≈ 5 300 €/год** |
| 4 | **Фактурация и relance impayés** | 1 чел. × 4 ч/нед, письма вручную, нерегулярно | Ежедневный прогон по возрасту долга, персонализированные relance по эскалации, ответы на «где счёт?» | −60 %: 2,4 ч/нед → **≈ 3 240 €/год** + эффект на BFR: −5 дней DSO при CA 3 M€ ≈ **41 000 € высвобожденного оборотного капитала** |
| 5 | **Ведение каталога и цен** | 1 чел. × 5 ч/нед: прайсы поставщиков в Excel, ручной перенос, описания товаров | Разбор прайс-листов поставщиков, обновление цен, генерация описаний и fiches techniques | −70 %: 3,5 ч/нед → **≈ 4 700 €/год** |

**Итого прямая экономия времени ≈ 39 000–45 000 €/год** = **+13–15 % к EBE** модельной компании, плюс разовое высвобождение ~41 000 € оборотного капитала. Косвенный эффект (не считаю в цифрах): быстрее devis → выше win rate.

**Пилот №1:** *приём заказа из email → черновик в ERP + автоматический ARC клиенту.*
Почему: единственный процесс, который виден в цифрах уже через 2 недели, не трогает бухгалтерию и не создаёт юридического риска.
**Метрики успеха (6 недель):** (1) доля заказов, попавших в ERP без ручной перепечатки ≥ 70 %; (2) медианное время от входящего письма до ARC клиенту < 2 рабочих часов (базовая замеряется в первую неделю); (3) число ошибок ввода (неверный код/количество) −50 % к базе.

**Черновик первого письма (не отправлено):**

> Objet : gagner 2 jours par semaine sur la saisie des commandes
>
> Bonjour Monsieur X,
>
> Je m'appelle Maxime, je travaille sur l'automatisation des tâches administratives dans les PME de négoce en Île-de-France.
>
> Dans une entreprise de votre taille, la saisie des commandes reçues par e-mail, la préparation des devis et les relances occupent souvent l'équipe ADV plusieurs jours par semaine. Ces tâches se traitent aujourd'hui automatiquement, sans changer votre ERP.
>
> Je vous propose un audit gratuit d'une à deux heures, dans vos locaux : nous regardons ensemble vos trois processus les plus lourds et je vous remets une estimation chiffrée du temps récupérable. Sans engagement.
>
> Seriez-vous disponible pour un échange de 20 minutes ?
>
> Bien cordialement,
> Maxime — [téléphone] — [email]

*(114 слов)*

---

### 5.2 Propreté / nettoyage / facility

**Модельная компания:** CA 1,5 M€, ~55 агентов (большинство на частичной занятости), 5 сотрудников офиса (1 responsable d'exploitation, 1 chargé de planning, 1 assistante administrative, 1 compta/paie, 1 dirigeant). EBE **оценка** 6 % CA = 90 000 €.

| # | Процесс | Как устроено сейчас | Что делает агент | Экономия (**оценка**) |
|---|---|---|---|---|
| 1 | **Планирование и замена отсутствующих агентов** | responsable d'exploitation ~10 ч/нед: звонки, SMS, перекройка графика при каждом отсутствии | Предлагает замену по близости, квалификации, доступности и рабочему времени; рассылает предложения и фиксирует подтверждения | −40 %: 4 ч/нед → **≈ 6 300 €/год** |
| 2 | **Pointage → переменная часть зарплаты** | assistante 8 ч/нед: сбор листов/телегестии, сверка с графиком, подготовка переменных для paie | Сверка фактических часов с графиком, автоматическое выделение аномалий, готовый файл переменных | −60 %: 4,8 ч/нед → **≈ 6 050 €/год** |
| 3 | **Devis по входящим запросам** | 6 ч/нед: выезд, замер, расчёт по площади/частоте/cadence, оформление | Черновик devis по площади, типу помещений и частоте на базе вашей сетки cadences; человек корректирует после визита | −50 %: 3 ч/нед → **≈ 4 320 €/год** |
| 4 | **Ежемесячная фактурация + relance impayés** | 7 ч/нед: сотни строк по договорам, avenants, prestations exceptionnelles, разрозненные relance | Сборка счётов из договоров + фактических вмешательств, проверка avenants, автоматические relance по эскалации | −65 %: 4,5 ч/нед → **≈ 5 670 €/год** |
| 5 | **Рекрутинг и первичный отбор** | 5 ч/нед: сортировка CV, обзвон, проверка доступности и зоны | Разбор CV и заявок, предквалификация по зоне/часам/опыту, планирование собеседований | −70 %: 3,5 ч/нед → **≈ 4 725 €/год** |

**Итого ≈ 27 000 €/год** = **+30 % к EBE** модельной компании. Это выше, чем в négoce, в относительном выражении именно потому, что EBE в propreté тонкий. Косвенные эффекты (не в цифрах): меньше несфактурированных prestations exceptionnelles, меньше пенальти за непокрытые объекты.

**Пилот №1:** *цикл ежемесячной фактурации + relance impayés.*
Почему: полностью измерим, ограничен по контуру, не трогает ни график агентов, ни расчёт зарплаты — то есть не создаёт социального риска в компании с высокой текучестью.
**Метрики успеха (3 месяца):** (1) часы на цикл фактурации −60 % (база — первый месяц); (2) счета выставлены до 3-го числа месяца в 100 % случаев; (3) DSO −5 дней за 3 месяца; (4) сумма prestations exceptionnelles, попавших в счёт, +10 % (раньше часть терялась).

**Черновик первого письма (не отправлено):**

> Objet : votre facturation mensuelle en deux fois moins de temps
>
> Bonjour Monsieur X,
>
> Je m'appelle Maxime, j'automatise les tâches administratives des entreprises de propreté en Île-de-France.
>
> Chez une société de votre taille, la facturation mensuelle, les relances et la gestion des remplacements prennent facilement une journée par semaine à votre équipe administrative. Ce travail peut être largement automatisé, avec vos outils actuels.
>
> Je vous propose un diagnostic gratuit d'une à deux heures, sur place : nous mesurons ensemble le temps réellement passé sur ces tâches et je vous remets un chiffrage du temps et du coût récupérables. Sans engagement, et vous gardez le document.
>
> Auriez-vous 20 minutes pour en parler ?
>
> Bien cordialement,
> Maxime — [téléphone] — [email]

*(113 слов)*

---

## 6. Чего не удалось найти / что закрыто — сводно

| Что | Статус | Обход, который я применил |
|---|---|---|
| Cessionpme.com | HTTP 403 на автоматический доступ | частично покрыт через агрегатор Bpifrance |
| Полные досье CRA (effectif, EBE) | закрыто членством | собраны публичные поля: NAF, motif de cession, CA, prix |
| Prix и effectif в списке Fusacq | видны только после входа в аккаунт | собраны activité, CA, регион, дата; prix взят с других площадок |
| Мультипликатор prix/EBITDA по отраслям | EBE есть лишь в 101 объявлении из 1 603 | использован **p/CA** (828 наблюдений) + внешние бенчмарки |
| Pappers.fr | HTTP 403 | официальный API recherche-entreprises.api.gouv.fr (те же данные RNE/INSEE) |
| Annuaire-entreprises.data.gouv.fr (веб) | анти-бот Incapsula | тот же официальный API |
| Indeed | HTTP 403 | отраслевые объёмы вакансий через France Travail |
| Welcome to the Jungle | HTTP 202 (анти-бот) | — |
| API France Travail (offres) | HTTP 401, нужен партнёрский ключ | публичный сайт candidat.francetravail.fr |
| LinkedIn компаний | требует входа в аккаунт (бриф запрещает регистрацию) | `n/d`, ручная проверка |
| Поле «зависимость от владельца» | ни одна площадка не публикует | косвенно — в `notes` (текст описания объявления) |
| DGE «baromètre transmission-reprise» как отдельный файл | опубликован как Théma n°30 | использован Théma n°30 (июнь 2025) |
| In Extenso «Régions & Transmission» полный PDF | доступен по форме регистрации | использован публичный пресс-релиз с цифрами |

---

## 7. Что я рекомендую сделать дальше

1. **Вручную дообогатить 20 компаний приоритета A** (по 10 на отрасль): LinkedIn, сайт, вакансии на `candidat.francetravail.fr`, структура акционеров в RNE. Это ~4 часа работы и снимает единственный существенный пробел в данных.
2. **Начать с propreté** — 52 компании приоритета A в IdF, слабейшая цифровизация, самый низкий порог входа в разговор.
3. **Измерять в первом же визите** доли времени из таблиц §5 — мои цифры это оценка, а ваше коммерческое предложение должно опираться на замер у клиента. Этот замер и есть продукт бесплатного разбора.
4. **Если готовы сдать экзамен на attestation de capacité de commissionnaire** — пересмотреть транспорт как вторую отрасль вместо propreté: объём предложения втрое больше при той же устойчивости к AI.
