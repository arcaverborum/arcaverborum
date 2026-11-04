# VERIFY — lafone1895

## Pages

Printed pp. 113–121 = PDF pp. 113–121 of BIGA tomo XVI (sha256 `fc0f9a09…4b1b4b`); Chulupí–Español pp. 113–117, Español–Chulupí pp. 118–121.

## Procedure

* **Pass 1.** Each page was rendered as four column crops (left/right × upper/lower half) at 400 dpi. Doubtful spots were re-rendered at 600–1000 dpi. Every printed entry was transcribed into a working table: page, direction, full `Value`, forms, Spanish gloss, English, keep/skip decision and comment. The scan's OCR layer served only as a typing aid and was corrected against the image. It is wrong in many places, e.g. p. 120 *ó* for *é* throughout, *Ni-niumbapa* for *Ni-hiumbapa*, and *mina* vs *mmá*.
* **Pass 2 (separate re-reading; not strictly blind).** Each page was re-rendered with a different cut: column crops in thirds, 450 dpi. All Vilela forms of every entry, including skipped ones, were re-read from the image into a separate list per page, without consulting the pass-1 forms. The two lists were then compared mechanically, form by form, in page order (difflib).
  *Caveat:* the same agent did both passes, so its pass-1 transcription was still in its working context during pass 2. The re-reading was not strictly blind, and the low discrepancy count is probably optimistic. A blind re-check of a sample is advisable before promotion.
* **Rows checked:** all 654 printed entries (pass-1 entries and pass-2 entries agree in number on every page: 47, 80, 76, 79, 59, 69, 85, 92, 67) and all 759 Vilela form tokens, including those in skipped entries.

## Discrepancies and resolution

| page | pass 1 | pass 2 | resolution (zoomed at 900–1000 dpi) |
|---|---|---|---|
| 120 | *uyusé* (Oveja) | *oyusé* | image shows **u y u s é**; pass 1 kept |
| 120 | *nan-táte-mi* (tu Padre) | *nan-tàte-mi* | italic accent is clearly a **grave**; corrected to *nan-tàte-mi* |
| 119 | *úcope* (Flecha) | *úcope* (flagged doubtful) | zoom shows two dots: transcribed *ücope*, comment "unclear (damaged acute?)" |
| 116 | gloss *copulam habere* | *copulum habere* | italic is ambiguous (u/a); `Value` keeps *copulum habere*, parameter merged with ES–CH *Copulam habere*, comment added |
| 114 | *Gegdúb' mento* as a form | — | ES–CH p. 120 *Mento, gégdúb* shows that *mento* is the Spanish gloss printed in bold; form set to *Gegdúb'*, gloss *mento*, comment added |

Before pass 2, zooms confirmed these readings: *Nihthemuí* and *Níbutzeje* (bold *í*, not dotted *i*), *itzibep môhpa* (circumflex), *gále-moyáj* (initial *g*), *mmaic* (c/e unclear), *lœc nitemui* (œ), *olöh* (two dots), *Agua, mina, mmá*.

## Unclear readings (kept, flagged in `Comment`)

*mina* (possibly *mma*), *lœc nitemui*, *ajeté*, *ni-tuichué*, *tacá-hupp*, *mmaic, bumbápp*, *núhú* (accents), *olöh*, *ücope*, *gále-moyáj*, *copulum habere*. No row was dropped as unreadable.

## Counts

* printed entries: 654 (CE 341, EC 313); kept 493 entries, which give 582 form tokens before merging
* rows (`forms.csv`): **410**; distinct forms 407; rows attested in both directions 172, CE only 119, EC only 119
* distinct glosses (`parameters.csv`): **221**; Concepticon-mapped: **128**
* Loan = true: 4 rows (Ajbulún, Gato, Tahuaco, Vaca)
* skipped: phrase 141 (CE 65, EC 76); name/ethnonym/toponym 10; cross-reference only 7; editorial 2; mis-indexed 1 (total 161 entries)

## Integrity

`python3 -I tools/validate_ext.py lafone1895` (repo validator plus spec checks: NFC, empty Segments, Source keys, Concepticon ID/gloss pairs, `' | '` in names): 0 problems. All IDs are unique, every Language_ID and Parameter_ID resolves, and the only Source key is `lafone1895_lafonequevedo1895`, which is in `sources.bib`.

## Skipped entries

| page | dir | reason | printed entry |
|---|---|---|---|
| 113 | CE | skip:phrase | Ajbulin nuj-quiiribá, no quiero taparme, (Ywill not cover myself). |
| 113 | CE | skip:phrase | Aj-holimen uanoc-col, no mates los perros, (Do not kill the dogs). |
| 113 | CE | skip:phrase | Ajsab quiirubaj, no sé hablar cristiano. Y cannot speak the Christian's language. |
| 113 | CE | skip:phrase | Ajsábin nimcquié? Sabes hablar cristiano? Can you speak Christian etc. |
| 113 | CE | skip:phrase | Ajsálimén, no te bañes. Bathe not. |
| 113 | CE | skip:phrase | Aléi-u-uajemén, no comas el pájaro, do not eat the bird. |
| 113 | CE | skip:phrase | Ami-chquiiripaj / Ami-quiiripaj } no hay, there is none |
| 113 | CE | skip:phrase | Ccucu mmá, traigame agua. bring me water, (cquiitaj). |
| 113 | CE | skip:phrase | Colonias, ndeté quiitáj Colonias sláp, Ved ahí Pedro se vá para la Colonia, See Peter is off to the Colony. |
| 113 | CE | skip:phrase | Chquiirilcnum, alza este palo, vel ilc-num chquiiré, lift up this stick. |
| 114 | CE | skip:phrase | Ehé etemuinchquiij, si te quiero, yes I love thee. |
| 114 | CE | skip:phrase | Etépuis-sabganáj, vamos á dormir, let us go to sleep or to bed. |
| 114 | CE | skip:phrase | Hamól dobáj, ¿por qué no quiere? Why will he not? |
| 114 | CE | skip:phrase | Hguéb, boca del gato, cat's mouth. |
| 114 | CE | skip:name | Hitej, Rio Bermejo. |
| 114 | CE | skip:phrase | Hosnójóje, mañana vendrá, he comes tomorrow. |
| 114 | CE | skip:phrase | Huanelá chquiitaj, P. se vá á la ranchería, he is going away to the huts. |
| 114 | CE | skip:phrase | Huanj-col huupé laphé, pata de perro, dog's foot. |
| 114 | CE | skip:name | Huanuané, Tobas. |
| 114 | CE | skip:phrase | Iic-que-hóm, trabaja ligero, get on with your work. |
| 114 | CE | skip:phrase | Ilcnabépp icquiiguác, no puedo alzarlo, Y cannot lift it. |
| 114 | CE | skip:name | Iuen-nuanit, Matacos. |
| 115 | CE | skip:phrase | Kauuissat, Pablo es valiente, Paul is brave. |
| 115 | CE | skip:phrase | Lacque qui-cquiu aj, yo quiero comer, I want something to eat. |
| 115 | CE | skip:phrase | Lacquemi cquiulquié?, ¿quiéres comer?, ¿will you have something to eat? |
| 115 | CE | skip:phrase | Lajetenáj bitáj, tengo hambre, I am hungry. |
| 115 | CE | skip:phrase | Lájeuéyaj, porque es un cobarde, because he is a coward. |
| 115 | CE | skip:phrase | Liháj, porque es muy pesado, because it is very heavy. |
| 115 | CE | skip:editorial | Lule maslup, ver tu oreja, dudoso; doubtful. |
| 115 | CE | skip:phrase | Maijlumétequeyáj, tus orejas están limpias, thy ears are clean. |
| 115 | CE | skip:phrase | Mamicchquiucquié?, ¿quiéres beber?, have a drink? |
| 115 | CE | skip:phrase | Manaj-su-tu-laj, tengo sed. I am thirsty. |
| 115 | CE | skip:phrase | Manojquiaj, yo quiero beber, I want a drink. |
| 115 | CE | skip:phrase | Manojquilopáj, no quiero beber, I do not want a drink. |
| 115 | CE | skip:phrase | Namhuinquiaj, no te quiero, I love thee not. Vel nampasquiaj. |
| 115 | CE | skip:phrase | Namilaj?, ¿Cómo te vá? how farest thou? |
| 115 | CE | skip:name | Natocóit, Tobas. |
| 116 | CE | skip:phrase | Ni-temu-cquiéhit, hombre grande, big man. |
| 116 | CE | skip:phrase | Nohúm nihié, dame fuego, give me a light. |
| 116 | CE | skip:phrase | Nójhuim ni-hié, deme fuego, please—Vel ni-hié noj-om, give me a light. |
| 116 | CE | skip:xref | Nuj quiiribá, ver Ajbulin. |
| 116 | CE | skip:phrase | Oiyusé, oué, muchas ovejas, many sheep, a flock. |
| 116 | CE | skip:phrase | Pedro-ni-teropaj, Pedro no quiere venir, Pedro will not come. |
| 116 | CE | skip:phrase | Pedro Tata, el padre de Pedro, Petér's father. |
| 116 | CE | skip:phrase | Pedro uampé, el rancho de Pedro, Petér's hut. |
| 116 | CE | skip:phrase | Peigro étemaijlu-tequeyaj, las orejas de Pedro están limpias, Petér's ears are clean. |
| 116 | CE | skip:phrase | Pei-jlop, étémancquief, no, he bebido; no, I have had a drink. |
| 116 | CE | skip:phrase | Pe-jlóp, etelaquicquiin, no, he comido; no, I have eaten. |
| 116 | CE | skip:phrase | Peijlop gaguif, no, porque no puedo, no, because I cannot. |
| 116 | CE | skip:phrase | Pelinaj uuisságóm, vete á dormir, go to bed. |
| 116 | CE | skip:phrase | Pelinaj, quiero dormir contigo, I want to sleep with thee. |
| 116 | CE | skip:phrase | Quiánojnite-cquié?, quieres venir conmigo? will you come with me? |
| 116 | CE | skip:xref | Quiirubaj, ver Ajsab. |
| 116 | CE | skip:phrase | Sapé huumpé, el tiempo de las flores, flower season. |
| 116 | CE | skip:phrase | Taj-la-chée, adonde está Pedro? where is Peter? |
| 116 | CE | skip:phrase | Tata inj-chla, mi padre viejo, u? my old father. |
| 116 | CE | skip:phrase | Tchitaj, ya se ha ido, he is already gone away, vel tquitáj. |
| 116 | CE | skip:phrase | Tóláj, porque está enfermo, because he is ill. |
| 117 | CE | skip:phrase | Tucquimén; ó pojanén, no disparen (muchachos) don't run away (boys). |
| 117 | CE | skip:phrase | Tu-hue huuáj, no tengo ese, I, have not that one. |
| 117 | CE | skip:phrase | Uájbét un-nom, deme comida, give me my dinner. |
| 117 | CE | skip:phrase | Uájnójquilopaj, no quiero comer, I will not eat. |
| 117 | CE | skip:phrase | Uamcquiimbápp, casa grande, big house. |
| 117 | CE | skip:phrase | Uáno-col ipé. pescuezo de perro, vel ibep, dog's neck. |
| 117 | CE | skip:phrase | Uanoc, col ajbúm. mata el perro, kill the dog. |
| 117 | CE | skip:phrase | Uanoc-col ajbeméro, no mates el perro, do not kill the dog. |
| 117 | CE | skip:phrase | Ubépp injchlá, padre viejo, old father. P. |
| 117 | CE | skip:name | Uic-nii, Chiriguano. |
| 117 | CE | skip:phrase | Umbapá iu-heié, cacique general. |
| 117 | CE | skip:phrase | Umbatpá ajiuj huaj, está con el cacique, he is with the cacique. |
| 117 | CE | skip:phrase | Um hinit nem?, ¿me quieres?, dost love me? |
| 117 | CE | skip:phrase | Un-nom a-te, traeme agua, bring me water. |
| 117 | CE | skip:phrase | Upilemm pójáj, los muchachos están disparando, the boys are running away. |
| 117 | CE | skip:editorial | Yulo-naptorit, yulos-naptorita úhué, pájaros lacustres grandes y zancudos. |
| 118 | EC | skip:phrase | A dónde está Pedro? taj-la-chée. |
| 118 | EC | skip:phrase | Alzarlo no puedo, ilcnabépp icquiiguác |
| 118 | EC | skip:phrase | Alza este palo, chquiirilc-num, vel ilc-num, chquiiré. |
| 118 | EC | skip:phrase | Báñes-no te, ajsalimén. |
| 118 | EC | skip:phrase | Beber no quiero, manojqui-lopáj. |
| 118 | EC | skip:phrase | Beber yo quiero, manojquiaj. |
| 118 | EC | skip:phrase | Bebido no he, pei-jlop: étémancquief. |
| 118 | EC | skip:phrase | Boca del gato, hpuéb (boca, mostrando un gato. |
| 118 | EC | skip:phrase | Cacique general, umbapá-iu-heié. |
| 118 | EC | skip:phrase | está con el Cacique, umbatpá ajiu-huaj |
| 118 | EC | skip:phrase | Casa grande, uamcquiimbápp (?) P. |
| 118 | EC | skip:phrase | no Comas el pájaro, a-léi-u-uajemén. |
| 118 | EC | skip:phrase | ¿quieres Comer? lacquemi cquiulquié? |
| 118 | EC | skip:phrase | no; he Comido, pei-lop: ete la quicquiin vel ndetigaquiij. |
| 118 | EC | skip:phrase | no quiero Comer, uájnoj-quilopaj. |
| 118 | EC | skip:xref | yo quiero Comer, ver yo quiero comer. |
| 118 | EC | skip:phrase | Cómo te vá? namiláj. |
| 118 | EC | skip:xref | Conmigo, ver quieres venir. |
| 119 | EC | skip:phrase | no sé hablar Cristiano, ajsab quiirubáj |
| 119 | EC | skip:xref | ¿sabes hablar Cristiano? ver sabes hablar. |
| 119 | EC | skip:name | Chiriguanos, uicnii. |
| 119 | EC | skip:phrase | Dame fuego, nohúm nihié. |
| 119 | EC | skip:phrase | Deme comida, uajhét un-nom. |
| 119 | EC | skip:phrase | Deme fuego, nójhuim ni-hié, vel ni-hié noj-óm. |
| 119 | EC | skip:phrase | no Disparen (muchachos), tucquimén, pojamén. |
| 119 | EC | skip:phrase | quiero Dormir contigo, pélináj. |
| 119 | EC | skip:phrase | vete á Dormir, pelinaj uuissagom. |
| 119 | EC | skip:phrase | por qué está Enfermo, toláj. |
| 119 | EC | skip:phrase | Está con el cacique, umbatpá ajiú-huaj |
| 119 | EC | skip:misindexed | Grande, uamcquiimbápp. |
| 119 | EC | skip:phrase | ¿Sabes hablar cristiano?, ajsábin nimcquié? |
| 119 | EC | skip:phrase | No sé hablar cristiano, ajsáb quiirubáj. |
| 119 | EC | skip:phrase | No hay, amiquiiripáj. |
| 119 | EC | skip:phrase | No hay, ami-chquiiripáj. |
| 119 | EC | skip:phrase | Hombre grande, ni-temú, cquiéhit. |
| 119 | EC | skip:phrase | Ya se ha ido, tchitáj, vel tquitáj. |
| 119 | EC | skip:phrase | Mañana vendrá, hosnójeje. |
| 119 | EC | skip:name | Matacos, iuennuanit. |
| 119 | EC | skip:phrase | Mata el perro, uanoc-col, ajbúm. |
| 119 | EC | skip:phrase | No mates el perro, uanoc-col, ajbemén. |
| 120 | EC | skip:phrase | No mates los perros, aj-holimén, uanoc-col. |
| 120 | EC | skip:phrase | Losmuchachos están disparando, úpilémm pójáj. |
| 120 | EC | skip:xref | No disparen muchachos, Ver, nó disparen. |
| 120 | EC | skip:phrase | Muchas ovejas, oiyusé o-ué. |
| 120 | EC | skip:phrase | No, porque no puedo, peijlop gaquij. |
| 120 | EC | skip:phrase | tus Orejas están limpias, maijlumétequeyáj. |
| 120 | EC | skip:phrase | las Orejas de Pedro están limpias, Peigro étemáijlu-téqueyáj. |
| 120 | EC | skip:phrase | Pablo es valiente, Kauuissat. |
| 120 | EC | skip:phrase | el Padre de Pedro, Pedro tata. |
| 120 | EC | skip:phrase | mi Padre viejo, tata injchlá. |
| 120 | EC | skip:phrase | Padre viejo, ubépp injchlá (P). |
| 120 | EC | skip:phrase | Pata de perro, huanj-col huupé laphé. |
| 120 | EC | skip:phrase | Pedro se va á la ranchería, huanelá chquiitaj. |
| 120 | EC | skip:phrase | Pedro no quiere venir, Pedro ni-téropaj |
| 120 | EC | skip:phrase | Pescuezo de perro, uáno-col ipé; vel ibep. |
| 120 | EC | skip:phrase | ¿Porqué no quiere? hámól-dóbáj? |
| 120 | EC | skip:phrase | Porque es muy pesado, liháj. |
| 120 | EC | skip:phrase | Porque es un cobarde, lájeuéyaj. |
| 120 | EC | skip:phrase | Porque está enfermo, tóláj. |
| 120 | EC | skip:phrase | no Puedo alzarlo, ilcnabépp icquiyuác. |
| 120 | EC | skip:phrase | Quieres comer? lacquemi cquiulquié? |
| 120 | EC | skip:phrase | Quieres beber? mamicch-quiucquié? |
| 120 | EC | skip:phrase | Quieres venir conmigo? quiánojnite-cquié? |
| 120 | EC | skip:phrase | me Quieres, umhinit nem? |
| 120 | EC | skip:phrase | no Quiero taparme, ajbulin nuj-quiiribá |
| 120 | EC | skip:phrase | si te Quiero, èhe etemuinch-quiij. |
| 120 | EC | skip:phrase | yo Quiero comer, lacque qui-cquiúaj. |
| 120 | EC | skip:phrase | yo Quiero beber, manojquiáj, |
| 120 | EC | skip:phrase | yo Quiero beber, manojquilopaj. |
| 120 | EC | skip:phrase | no te Quiero, namhuinquiaj: vel nampasquiaj. |
| 120 | EC | skip:phrase | no Quiero comer, uajnojquilopaj. |
| 121 | EC | skip:phrase | el Rancho de Pedro, Pedro uampé. |
| 121 | EC | skip:name | Rio Bermejo, hitej. |
| 121 | EC | skip:xref | No quiero taparme, ver no quiero. |
| 121 | EC | skip:phrase | Tengo hambre, lajetenaj, bitaj. |
| 121 | EC | skip:phrase | no Tengo, iyaj. vel amadúblé. |
| 121 | EC | skip:phrase | no Tengo ese, tu hue huuáj. |
| 121 | EC | skip:phrase | Tengo sed, manaj-su-tu-baj. |
| 121 | EC | skip:phrase | el Tiempo de las flores, sapé huumpé. |
| 121 | EC | skip:name | Tobas, Huanûané. |
| 121 | EC | skip:name | Tobas, Na-tocóit. |
| 121 | EC | skip:phrase | Trabaja ligero, iicque-hóm. |
| 121 | EC | skip:phrase | Traeme agua, un-nom á-té. |
| 121 | EC | skip:phrase | Traigame agua, ccucu mmá. |
| 121 | EC | skip:phrase | Vamos á dormir, etépuis sabganáj. |
| 121 | EC | skip:phrase | Ved ahi Pedro se va para la Colonia, ndete cquiitá Colonias-sláp. |
| 121 | EC | skip:phrase | Vete á dormir, pelinaj uuisságóm. |
