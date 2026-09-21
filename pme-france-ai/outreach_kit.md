# outreach_kit.md — техническая реализуемость и набор для первого контакта

**Дата: 21 сентября 2026.** «Факт» = данные из источника с URL. «Оценка» = мой вывод.
Все тексты на французском — **черновики. Ничего не отправлено.**

---

# Часть I. Техническая реализуемость (этап E)

> Принцип: агент бесполезен, если не может прочитать и записать в систему клиента. Поэтому сначала — какие системы реально стоят у французских PME этого размера, что у них открыто, и какие процессы можно взять **без интеграции с ядром**.

## 1. Что стоит у французских PME 10–50 человек

**Оговорка (важно).** Публичной статистики «какой ERP стоит у PME такого-то размера» во Франции нет. Ниже — сведение данных вендоров, отраслевых обзоров и моей собственной проверки 31 сайта компаний из `top15_*.md`: **ни один из 31 сайта не называет используемую систему.** Поэтому доля рынка — **оценка**, а не факт. Достоверны только сведения о наличии и открытости API, они взяты с документации вендоров.

### Négoce / distribution B2B

| Система | Распространённость (оценка) | Облако / on-premise | API | Документация | Практический вывод |
|---|---|---|---|---|---|
| **Sage 100** | Очень высокая — исторический стандарт для французских PME 10–100 чел. с сильной бухгалтерией и коммерческим управлением | Преимущественно **on-premise** (есть «cloud-hosted») | **Нативного REST API нет.** Интеграция через **BOI (Business Object Interface)** и ODBC; REST-обёртки делают сторонние ISV | [Sage Community Hub — BOI и варианты API](https://communityhub.sage.com/us/sage100/f/business-object-interface/133666/api-documentation---sage-100); обзор [Kissinger](https://www.kissingerassoc.com/blog/sage100-api) | **Худший случай для интеграции.** Прямой записи в ядро без ISV-прослойки нет → начинать только на уровне почты/файлов |
| **EBP Gestion Commerciale** | Высокая в сегменте TPE/малые PME. EBP поглощён Cegid | SaaS и локальная подписка | **REST API есть** для SaaS-продуктов (с v21.1). Доступ требует активного контракта поддержки; портал разработчиков закрыт для партнёров/реселлеров | [developpeurs.ebp.com](https://developpeurs.ebp.com/) · [справка EBP по REST API](https://support.ebp.com/hc/fr/articles/4419126485649-API-Rest-qu-est-ce-que-le-Portail-d%C3%A9veloppeur-EBP) | API есть, но **доступ платный и через партнёрский статус** — закладывать срок на получение |
| **Cegid XRP Flex / Cegid Loop** | Средняя и растущая (Cegid консолидирует рынок, купив EBP) | **100 % облако** | **REST API, входящие и исходящие**, публичный портал разработчиков, примеры на GitHub | [developers.cegid.com](https://developers.cegid.com/) · [Loop API](https://developers.cegid.com/docreference/BusinessUnits/Loop-Api-Management-Docs/index.html) · [cegid-xrp-flex-api-samples (GitHub)](https://github.com/cegid-io/cegid-xrp-flex-api-samples) | **Лучший случай.** Ключ выдаёт «référent Cegid» клиента |
| **Divalto infinity / weavy** | Средняя, сильна именно в négoce и дистрибуции | Облако и on-premise | **REST API** (POST + JSON, токен на 45 мин) и **OData** для чтения таблиц ERP/CRM | [Services Web (API) REST](https://divalto.atlassian.net/wiki/spaces/PAI/pages/10550740818/Services+Web+API+Architecture+REST) · [API OData weavy](https://divalto.atlassian.net/wiki/spaces/PAW/pages/10750328833/API+OData+Divalto+weavy) | Документация открыта и подробная — **вторая по удобству после Cegid** |
| **Microsoft Dynamics 365 Business Central** | Средняя, чаще у PME с международными связями | Облако | Стандартные REST/OData API Microsoft | Документация Microsoft Learn | Технически проще всего, но реже встречается в независимых PME |
| **Odoo** | Растущая у молодых PME | Облако и on-premise | Открытый XML-RPC/JSON-RPC | Официальная документация Odoo | Легко интегрируется; редко у компаний 1970–1990 годов основания |

### Transport / commissionnaires

| Система | Распространённость (оценка) | Облако / on-premise | API | Документация | Практический вывод |
|---|---|---|---|---|---|
| **Akanea TMS** (Start / Freight Forwarding / XROAD) | Очень высокая у французских TPE/PME транспорта и комиссионеров | Облако и on-premise в зависимости от линейки | **«API Select»** — модуль стандартных API, 6 семейств данных (заказы, статусы, клиенты и т. д.) | [Akanea — API Select](https://akanea.com/api-select-lancement/) · [Akanea TMS Freight Forwarding](https://akanea.com/en/solutions/tms-freight-forwarding/) | API продаётся **как отдельный модуль** — у клиента его может не быть. Уточнять до обещаний |
| **Dashdoc** | Растущая, новое поколение | Облако | **Открытое публичное REST API v4**, документация в открытом доступе, готовые интеграции (Transporeon, Shippeo, Peppol, телематика) | [developer.dashdoc.com](https://developer.dashdoc.com/docs) · [API reference](https://www.dashdoc.eu/api/v4/docs/) | **Лучший случай в транспорте.** Документация читается без контракта |
| **DDS Supply Chain / Descartes** | Средняя, чаще у более крупных | Облако | API есть, документация по запросу | Сайт вендора | Средняя открытость |
| **Shiptify** | Средняя, сегмент грузовладельцев | Облако | API есть | Сайт вендора; тариф €150–3 000/мес | Скорее у chargeurs, чем у комиссионеров |
| **Transporeon** | Низкая у PME — платформа для крупных | Облако | API есть | Сайт вендора | Для PME избыточна |
| **Excel + почта без TMS** | **Оценка: заметная доля компаний до €5 млн** | — | — | — | Отсутствие системы — не препятствие, а самый лёгкий случай |

## 2. Общий фактор, который меняет расклад в 2026–2027: электронная фактура

**Факт.** Обязанность **принимать** электронные счета наступает для **всех** французских компаний **с 1 сентября 2026 года**, независимо от размера. Обязанность **выставлять** — с 1 сентября 2026 для крупных компаний и ETI, и **с 1 сентября 2027 для PME и микропредприятий**. Передача идёт через сертифицированные платформы (**PDP**), их зарегистрировано более 70. С 1 сентября 2026 в счёте появляются четыре новых обязательных реквизита.
Источники: [economie.gouv.fr — всё о электронной фактуре](https://www.economie.gouv.fr/tout-savoir-sur-la-facturation-electronique-pour-les-entreprises) · [impots.gouv.fr — практическое руководство к 01.09.2026 (PDF)](https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/guide_pratique_facturation_electronique.pdf) · [Service-Public Entreprendre](https://entreprendre.service-public.gouv.fr/actualites/A18953)

**Почему это важно вам (оценка).** Каждая компания из обоих списков **обязана** в ближайшие 12 месяцев пересмотреть свой цикл фактурации. Это: (1) готовый повод для холодного письма, не требующий продавать «AI»; (2) момент, когда данные счетов становятся структурированными — а структурированные данные резко упрощают автоматизацию relance и сверки. **Не привязывайте пилот к соответствию реформе — это работа PDP, не ваша. Используйте её как повод для разговора.**

## 3. Процессы, которые можно автоматизировать БЕЗ интеграции с ядром

Критерий: процесс живёт в почте, PDF/Excel и таблицах — то есть его можно взять, ничего не записывая в ERP/TMS. Человек остаётся звеном, которое нажимает «подтвердить» в существующей системе.

### Négoce B2B — три кандидата на первый пилот

| # | Процесс | Вход | Выход | Почему без интеграции |
|---|---|---|---|---|
| **1** | **Разбор входящих заказов и запросов** | письма с PDF/Excel/текстом | структурированные строки заказа (референс, количество, адрес, срок) в таблице или черновике письма | Агент читает почтовый ящик и пишет в таблицу. ADV копирует готовую строку в ERP вместо набора с нуля. **Ничего не пишется в ERP автоматически** |
| **2** | **Relance impayés** | выгрузка баланса дебиторов (CSV из любой системы) + почтовый ящик | персонализированные письма по возрасту долга, ответы на «où en est ma facture ?» | Единственная запись в систему — отметка «relance отправлена», её делает человек. Выгрузка CSV есть в любой системе, включая Sage 100 |
| **3** | **Сверка ARC поставщиков** | подтверждения заказа от поставщиков (PDF в почте) + ваш исходный заказ | список расхождений по цене, количеству и дате | Сравнение двух документов, результат — отчёт. Запись в ERP не нужна вообще |

### Transport / commissionnaire — три кандидата

| # | Процесс | Вход | Выход | Почему без интеграции |
|---|---|---|---|---|
| **1** | **Разбор входящих ordres de transport и запросов на котировку** | письма с PDF/Excel | структурированная строка (origine, destination, poids, volume, incoterm, délai) + предзаполненный devis по вашей тарифной сетке | Читает почту, пишет в таблицу. Exploitant подтверждает и заносит в TMS |
| **2** | **Сборка досье счёта и relance** | счёт + ordre + lettre de voiture/CMR + POD, разбросанные по почте и папкам | собранный комплект на оспариваемый счёт + письмо-relance | Работа с документами, не с базой TMS |
| **3** | **Ответы на «où est ma marchandise ?»** | почтовый ящик + статусы (экспорт CSV или скриншот-таблица из TMS) | готовый черновик ответа клиенту со статусом и ожидаемым сроком | Статусы берутся из экспорта, ответ уходит из почты |

**Вывод (оценка).** Во всех шести случаях требуемая интеграция — это **доступ к почтовому ящику и к одной CSV-выгрузке**. Это снимает главный технический риск первого пилота и позволяет обещать срок 4–6 недель даже клиенту на Sage 100 без API.

---

# Часть II. Набор для первого контакта (этап F)

## 4. Одностраничное предложение (FR)

> **Titre : Automatiser le travail administratif de votre PME — sans changer votre logiciel**
>
> **Le constat**
> Dans une PME de négoce ou d'organisation de transport, une part importante du temps de l'équipe administrative passe à retranscrire à la main ce qui arrive par e-mail : commandes, demandes de devis, confirmations fournisseurs, ordres de transport, relances. Ce travail est répétitif, il ne se facture pas, et il est aujourd'hui automatisable.
>
> **Ma proposition, en trois étapes**
>
> **1 — Diagnostic gratuit (1 à 2 heures, dans vos locaux)**
> Nous regardons ensemble vos trois flux les plus lourds. Je repars avec des volumes réels (nombre d'e-mails, de devis, de commandes par jour) et le temps passé, mesuré, pas estimé. Vous recevez sous 5 jours un document d'une page : où part le temps, combien il coûte, ce qui est automatisable et ce qui ne l'est pas. **Ce document est à vous, sans contrepartie et sans engagement.**
>
> **2 — Pilote sur un seul processus (4 à 6 semaines, prix fixe)**
> Nous choisissons ensemble un processus : celui qui est le plus mesurable et le moins risqué. Je mesure d'abord la situation de départ, puis je livre l'automatisation, puis je mesure de nouveau. **Prix fixe annoncé avant de commencer, pas de régie, pas de dépassement.**
> Aucune modification de votre ERP ou de votre TMS n'est nécessaire : je travaille au niveau des e-mails, des documents et des fichiers d'export.
>
> **3 — Décision, sur des chiffres**
> À la fin du pilote, vous avez un tableau signé : heures avant, heures après, économie en euros sur l'année. Vous décidez alors d'étendre, de garder en l'état, ou d'arrêter. **Si le gain mesuré est inférieur à ce que j'ai annoncé au départ, vous ne payez pas la différence** (modalité précisée au §7).
>
> **Ce que je ne fais pas**
> Je ne remplace pas votre logiciel de gestion. Je ne touche pas à votre comptabilité. Je ne vends pas de licence : vous restez propriétaire de vos données et des automatisations mises en place.
>
> **Qui je suis**
> Maxime — AI Product Manager, basé à Paris. J'installe des agents d'intelligence artificielle et de l'analytique dans de grandes entreprises. Je travaille aujourd'hui avec des PME de négoce et d'organisation de transport en Île-de-France.

---

## 5. Опросник для первой встречи (23 вопроса, FR)

Сгруппирован. **Цель — получить цифры, а не мнения.** Вопросы 1–6 дают объём, 7–13 — систему, 14–18 — время, 19–23 — решение.

### A. Volumes (5 min)
1. Combien de demandes entrantes recevez-vous par jour, tous canaux confondus (e-mail, téléphone, portail) ?
2. Sur ces demandes, combien deviennent un devis ? Combien deviennent une commande ou un ordre ?
3. Combien de devis établissez-vous par semaine ? Et combien de factures par mois ?
4. Quelle part arrive par e-mail, par téléphone, par portail client, par EDI ? *(demander un ordre de grandeur en %)*
5. Combien de références / destinations différentes traitez-vous couramment ?
6. Y a-t-il des pics — fin de mois, saison, salons — où le volume double ?

### B. Qui fait quoi (5 min)
7. Combien de personnes touchent une demande entre son arrivée et la facture ?
8. Qui saisit la commande ou l'ordre ? Est-ce la même personne qui établit le devis ?
9. Que se passe-t-il quand cette personne est absente une semaine ?

### C. Systèmes (10 min — le plus important)
10. Quel logiciel de gestion utilisez-vous (ERP / TMS / gestion commerciale) ? Depuis quelle année ?
11. Est-il installé chez vous ou hébergé chez l'éditeur ?
12. Pouvez-vous exporter une liste — commandes, factures, balance clients — en Excel ou CSV vous-même, sans appeler votre prestataire ?
13. Avez-vous déjà un accès API ou un module de connexion avec ce logiciel ? Si oui, lequel ?
14. Vos e-mails professionnels sont-ils sur Microsoft 365, Google Workspace, ou autre chose ?
15. Où en êtes-vous de la facturation électronique obligatoire ? Avez-vous déjà choisi une plateforme ?

### D. Où ça coince (10 min)
16. Sur une semaine normale, combien d'heures votre équipe passe-t-elle à ressaisir des informations reçues par e-mail ? *(si la réponse est « je ne sais pas » : proposer de compter sur 3 jours)*
17. Quel est votre délai moyen entre la réception d'une demande et l'envoi du devis ? Et votre objectif ?
18. Quel type d'erreur revient le plus souvent : référence, quantité, prix, adresse, délai ?
19. Combien de factures sont contestées ou payées en retard chaque mois ? Qui relance, et à quelle fréquence ?
20. Quelle tâche administrative votre équipe déteste le plus ?

### E. Décision (5 min)
21. Avez-vous déjà tenté d'automatiser quelque chose ? Qu'est-ce qui n'a pas marché ?
22. Qui décide d'un budget de 10 000 € chez vous — vous seul, ou avec quelqu'un d'autre ?
23. Si on démarrait, quel mois serait le bon — et quel mois serait le pire ?

**Совет по ведению (оценка).** Вопрос 16 — центральный, и на него почти никогда нет готового ответа. Если владелец не знает — предложите измерить: попросите одного сотрудника три дня отмечать в простой таблице время на ввод. Это и есть содержание бесплатного разбора, и это то, что делает предложение конкретным.

---

## 6. Шаблон замера пилота

Это тот документ, который клиент подписывает в конце и который становится вашим кейсом. Заполняется **дважды**: baseline до старта и результат после.

### Лист 1 — Périmètre
| Поле | Значение |
|---|---|
| Entreprise / SIREN | |
| Processus retenu | (ex. traitement des commandes reçues par e-mail) |
| Personnes concernées | (nombre, fonctions) |
| Période de mesure initiale | (du … au …, minimum 10 jours ouvrés) |
| Période de mesure finale | (du … au …, même durée, même saisonnalité) |
| Systèmes touchés | (aucune écriture dans l'ERP : oui / non) |

### Лист 2 — Baseline → Résultat
| Indicateur | Comment il se mesure | Avant | Après | Écart |
|---|---|---|---|---|
| **Volume traité** — nombre d'unités (commandes / devis / factures) sur la période | comptage dans l'export | | | |
| **Temps total consacré** — heures sur la période | relevé par les personnes concernées | | | |
| **Temps par unité** — minutes | temps total ÷ volume | | | |
| **Part traitée sans ressaisie manuelle** — % | comptage | 0 % | | |
| **Délai de réponse au client** — heures ouvrées médianes entre réception et réponse | horodatage des e-mails | | | |
| **Erreurs détectées** — nombre (référence, quantité, prix, adresse, délai) | relevé | | | |
| **DSO** — jours *(si le pilote porte sur la relance)* | comptabilité | | | |

### Лист 3 — Chiffrage
| Ligne | Formule | Valeur |
|---|---|---|
| Heures économisées par semaine | (temps par unité avant − après) × volume hebdomadaire ÷ 60 | |
| Coût horaire chargé retenu | à convenir ensemble avant le pilote | … €/h |
| **Économie annuelle en euros** | heures économisées/semaine × 45 semaines × coût horaire | **… €** |
| Trésorerie libérée *(pilote relance)* | CA annuel ÷ 365 × jours de DSO gagnés | … € |
| Coût du pilote | prix fixe convenu | … € |
| **Retour sur investissement** | économie annuelle ÷ coût du pilote | **… ×** |

### Лист 4 — Validation
> « Les chiffres ci-dessus ont été relevés conjointement sur les périodes indiquées et reflètent l'activité réelle de l'entreprise. »
> Nom, fonction, date, signature du dirigeant. Case à cocher : ☐ j'autorise la publication de ces chiffres sous forme anonyme ☐ avec le nom de l'entreprise ☐ non.

**Почему последний пункт критичен (оценка).** Без письменного разрешения на публикацию кейс не поможет ни следующему клиенту, ни банку. Просить разрешение нужно **до** пилота, когда клиент в хорошем настроении, а не после.

---

## 7. Ценовые ориентиры и вилка

### Что видно на рынке (факт, с оговоркой о характере источников)

**Оговорка.** Ниже — публичные прайс-ориентиры. Барометр Malt — отраслевой справочник платформы фрилансеров; остальные ссылки — сайты агентств и консультантов, то есть **предложение, а не статистика сделок**. Независимой статистики цен на AI-пилоты для французских PME я не нашёл.

| Позиция | Ориентир | Источник |
|---|---|---|
| TJM фрилансера data/AI во Франции, 2026 | средний ~700 €/день; диапазон 450 → 1 000+ €/день по опыту и специализации | [Malt — барометр тарифов, эксперты data](https://www.malt.fr/t/barometre-tarifs/expert-data) (страница отдаёт 403 для автоматического доступа — открывать вручную); сводки [freelance-solution.fr](https://www.freelance-solution.fr/barometre-tjm-freelance-2026/) |
| TJM специалиста именно по AI/автоматизации | 750–1 500 €/день; профили MLOps и генеративного AI — 800–900 €/день | [studeria.fr — TJM consultant IA 2026](https://www.studeria.fr/articles-de-blog/tjm-consultant-ia-2026-tarifs-grille), [adapte-toi.com](https://adapte-toi.com/blog/tarifs-freelance-ia-grille-complete-specialite/) |
| Аудит AI | 2 000–5 000 € (диапазон 1 500–10 000 € в зависимости от размера) | [jaikin.eu — coût consultant IA](https://www.jaikin.eu/blog/cout-consultant-ia) |
| **POC / пилот** | **5 000–15 000 €** | там же |
| Простая автоматизация (сортировка почты, извлечение из документов, relance) | 2 000–8 000 € | [studioabis.com](https://studioabis.com/prix-automatisation-ia-pme), [autom-ia.com](https://autom-ia.com/blog/combien-coute-automatisation-ia-tpe-pme-2026/) |
| Проект PME с интеграцией CRM и разработкой | от 15 000–20 000 € | [studioabis.com](https://studioabis.com/prix-automatisation-ia-pme) |
| Подписка на поддержку | от 300–500 €/мес | там же |

### Моя рекомендация по вилке (оценка)

**Бесплатный разбор: 0 €.** Это не «бесплатная консультация», а покупка права на измерение. Ограничьте 2 часами и одностраничным результатом, иначе он съест ваше время.

**Пилот — три ступени по размеру клиента:**

| Профиль клиента | Цена пилота | Обоснование |
|---|---|---|
| CA < 3 млн € (напр. SERVIAPLUS, TRANSEXPO) | **5 000 €** | При EBE в десятки тысяч евро €10 тыс. — заметная трата. Нижняя граница рыночной вилки |
| CA 3–10 млн € (большинство списка) | **8 000–10 000 €** | Центр рыночной вилки POC. Окупается при экономии 250–350 часов в год |
| CA > 10 млн € (CGFP, MARSEILLE FRET, ATF, CEDIP) | **12 000–15 000 €** | Верх вилки оправдан объёмом: в компании с €15–25 млн те же 4–6 недель дают кратно больший абсолютный эффект |

**Вариант «фикс + процент от подтверждённой экономии».**
Формула: **фикс 5 000 € + 20 % от подтверждённой годовой экономии, с потолком 15 000 € в первый год**, выплата — через 3 месяца после окончания пилота, по цифрам из листа 3 шаблона замера.

- *Когда предлагать:* клиенту с тонкой маржой (TENDANCIEL DECOR 0,5 %, AUX DOCKS 0,2 %, SOGEMAT 1,1 %) — там €10 тыс. авансом воспринимаются тяжело, а доля от подтверждённого результата — нет.
- *Когда не предлагать:* клиенту с рентабельностью 11–16 % (CHRISTIAN RECUPER, CLAMAGERAN, MARSEILLE FRET) — им проще заплатить фикс, и вы не рискуете спором о цифрах.
- **Риск, который надо назвать вслух (оценка):** процент от экономии превращает замер в предмет торга. Поэтому **методика замера и ставка часа фиксируются письменно ДО старта**, в листе 1 шаблона. Без этого схему не предлагать.

**Чего не делать.** Не продавать по TJM (régie) на первом проекте: владелец PME не умеет оценивать риск открытой сметы и откажется. Фиксированная цена за названный результат — единственный формат, который проходит на холодном контакте.

---

## 8. Письма (FR, черновики — не отправлены)

Формат для каждой отрасли: первое письмо (**до 120 слов**), follow-up на 5-й день, follow-up на 12-й день. `[ACCROCHE]` — место для зацепки из карточки компании в `top15_*.md`. **Письмо без заполненной `[ACCROCHE]` не отправлять** — общая фраза про AI убивает всю серию.

### 8.1 Négoce B2B

**Письмо 1 — день 0 (118 слов)**

> Objet : combien d'heures par semaine passent en ressaisie de commandes ?
>
> Bonjour Monsieur/Madame [NOM],
>
> Je m'appelle Maxime, j'automatise le travail administratif des PME de négoce en Île-de-France.
>
> [ACCROCHE — 1 à 2 phrases sur un fait précis observé chez eux]
>
> Chez un négociant de votre taille, la saisie des commandes reçues par e-mail, la préparation des devis et les relances occupent souvent l'équipe ADV plusieurs jours par semaine. Ce travail s'automatise aujourd'hui sans changer votre logiciel de gestion.
>
> Je vous propose un diagnostic gratuit d'une à deux heures, dans vos locaux : nous mesurons le temps réellement passé et je vous remets un document d'une page. Sans engagement, et il est à vous.
>
> Auriez-vous vingt minutes pour en parler ?
>
> Bien cordialement,
> Maxime — [téléphone] — [e-mail]
> *Vous ne souhaitez plus recevoir de message de ma part ? Répondez « STOP » à cet e-mail.*

**Follow-up 1 — день 5 (68 слов)**

> Objet : Re: combien d'heures par semaine passent en ressaisie de commandes ?
>
> Bonjour Monsieur/Madame [NOM],
>
> Je reviens vers vous brièvement.
>
> Un chiffre pour situer : chez un négociant de 25 personnes, la ressaisie des commandes reçues par e-mail représente couramment l'équivalent d'un mi-temps. Le diagnostic que je propose sert d'abord à vérifier si c'est aussi votre cas — ou non.
>
> Deux heures, chez vous, sans engagement. Une date vous conviendrait-elle en [MOIS] ?
>
> Bien cordialement,
> Maxime
> *Répondez « STOP » pour ne plus être contacté.*

**Follow-up 2 — день 12 (74 слова)**

> Objet : dernier message — facturation électronique et ressaisie
>
> Bonjour Monsieur/Madame [NOM],
>
> Dernier message de ma part, je ne vous relancerai plus.
>
> Un point d'actualité qui peut vous intéresser : depuis le 1er septembre 2026, toutes les entreprises doivent pouvoir recevoir des factures électroniques, et les PME devront les émettre au 1er septembre 2027. Beaucoup de négociants en profitent pour revoir tout le cycle commande → facture.
>
> Si ce chantier est ouvert chez vous, mon diagnostic gratuit peut y contribuer. Sinon, je vous souhaite une bonne continuation.
>
> Bien cordialement,
> Maxime

### 8.2 Transport / commissionnaire

**Письмо 1 — день 0 (117 слов)**

> Objet : le temps passé à chiffrer une demande de transport
>
> Bonjour Monsieur/Madame [NOM],
>
> Je m'appelle Maxime, j'automatise le travail administratif des commissionnaires et organisateurs de transport en Île-de-France.
>
> [ACCROCHE — 1 à 2 phrases sur un fait précis observé chez eux]
>
> Dans une exploitation comme la vôtre, chaque demande arrive par e-mail et doit être relue, extraite — origine, destination, poids, délai — puis chiffrée à la main. Multiplié par le nombre de demandes quotidiennes, cela pèse lourd, et c'est aujourd'hui automatisable sans toucher à votre TMS.
>
> Je vous propose un diagnostic gratuit d'une à deux heures, sur place : nous mesurons le temps réel et je vous remets un document d'une page, sans engagement.
>
> Vingt minutes au téléphone cette semaine ?
>
> Bien cordialement,
> Maxime — [téléphone] — [e-mail]
> *Vous ne souhaitez plus recevoir de message de ma part ? Répondez « STOP ».*

**Follow-up 1 — день 5 (71 слово)**

> Objet : Re: le temps passé à chiffrer une demande de transport
>
> Bonjour Monsieur/Madame [NOM],
>
> Un exemple concret, pour être utile plutôt qu'insistant : reconstituer le dossier d'une facture contestée — ordre, lettre de voiture, preuve de livraison — prend souvent vingt à trente minutes à un exploitant. Sur un mois, cela fait plusieurs journées.
>
> Le diagnostic sert à savoir si ce poste pèse chez vous, et combien.
>
> Une date en [MOIS] vous irait-elle ?
>
> Bien cordialement,
> Maxime
> *Répondez « STOP » pour ne plus être contacté.*

**Follow-up 2 — день 12 (76 слов)**

> Objet : dernier message — relance et encours clients
>
> Bonjour Monsieur/Madame [NOM],
>
> Dernier message, je n'insisterai pas davantage.
>
> Dans l'organisation de transport, l'encours clients dépasse fréquemment 80 jours. Réduire ce délai de dix jours libère, pour 10 M€ de chiffre d'affaires, environ 270 000 € de trésorerie — sans vendre un euro de plus. C'est le chantier le plus rapide à mettre en place et le plus simple à mesurer.
>
> Si le sujet vous parle, je reste joignable. Sinon, bonne continuation à vous et à votre équipe.
>
> Bien cordialement,
> Maxime

---

## 9. Правила B2B-рассылки во Франции (CNIL)

**Источник:** [CNIL — La prospection commerciale par courrier électronique](https://www.cnil.fr/fr/la-prospection-commerciale-par-courrier-electronique). Правовая база: RGPD и art. L34-5 Code des postes et des communications électroniques.

### Что разрешено при холодном обращении к профессионалам (факт)

- **Предварительное согласие для B2B не требуется**, в отличие от B2C. Основание обработки — **законный интерес** (intérêt légitime), при условии что **содержание сообщения связано с профессией адресата**. Предлагать автоматизацию ADV директору négoce — связано. Предлагать ему что угодно личное — нет.
- **Общие адреса юридического лица** (`contact@`, `info@`, `commercial@`) **не считаются персональными данными**, так как относятся к компании, а не к человеку. Именно поэтому в обоих `top15_*.md` я собирал только общие адреса.
- **Именной профессиональный адрес** (`prenom.nom@entreprise.fr`) — **это персональные данные**, и к нему применяются все обязанности ниже.

### Что обязательно в каждом письме (факт)

1. **Идентификация отправителя** — кто пишет, от какой организации.
2. **Простой и бесплатный способ отказаться** от дальнейших сообщений. Для персональных адресов CNIL рекомендует незаполненную галочку отказа (case à cocher non pré-cochée); в переписке один на один достаточно явной фразы про отказ. В моих черновиках это строка *« Répondez STOP pour ne plus être contacté »*.
3. **Информирование в момент сбора адреса**: человек должен быть уведомлён о возможном использовании его адреса для prospection и иметь возможность возразить. **В холодной рассылке по данным из публичного реестра это уведомление даётся самим первым письмом** — поэтому оно и должно содержать пункт 1 и пункт 2 сразу.

### Как оформить opt-out на практике (оценка)

- **Ведите файл отказов.** Как только человек написал STOP или просто «не пишите больше» — занесите SIREN и адрес в отдельный список и **никогда** не отправляйте туда снова, в том числе по другому адресу той же компании. Это самая частая причина жалоб.
- **Соблюдайте отказ немедленно**, не «до конца текущей серии».
- **Право доступа и удаления.** Человек может запросить, какие его данные у вас есть, и потребовать удаления. Держите список источников по каждому контакту — у вас он уже есть в колонках `url_source_registre` и `url_source_finances`.
- **Ограничьте частоту.** Три письма за 12 дней и затем полная остановка — это то, что я заложил в черновики. Больше — риск жалобы, а не риск упущенной сделки.

### Дополнительные ссылки

- [CNIL — la prospection commerciale (dossier)](https://www.cnil.fr/fr/la-prospection-commerciale)
- [CNIL — обязанности по информированию лиц](https://www.cnil.fr/fr/linformation-des-personnes-concernees)

**Оговорка.** Это изложение публичных рекомендаций CNIL, а не юридическая консультация. Перед систематической рассылкой на именные адреса стоит проверить формулировки с юристом.
