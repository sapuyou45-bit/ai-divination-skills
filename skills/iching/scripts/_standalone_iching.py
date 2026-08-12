"""I Ching casting logic for package and CLI use."""

from __future__ import annotations

import argparse
import json
import random
from typing import Any


TRIGRAM_BITS = {
    "Heaven": "111",
    "Lake": "110",
    "Fire": "101",
    "Thunder": "100",
    "Wind": "011",
    "Water": "010",
    "Mountain": "001",
    "Earth": "000",
}

HEXAGRAMS = {
    ("Heaven", "Heaven"): (1, "Qian / The Creative"),
    ("Earth", "Earth"): (2, "Kun / The Receptive"),
    ("Water", "Thunder"): (3, "Zhun / Difficulty at the Beginning"),
    ("Mountain", "Water"): (4, "Meng / Youthful Folly"),
    ("Water", "Heaven"): (5, "Xu / Waiting"),
    ("Heaven", "Water"): (6, "Song / Conflict"),
    ("Earth", "Water"): (7, "Shi / The Army"),
    ("Water", "Earth"): (8, "Bi / Holding Together"),
    ("Wind", "Heaven"): (9, "Xiao Chu / Small Taming"),
    ("Heaven", "Lake"): (10, "Lu / Treading"),
    ("Earth", "Heaven"): (11, "Tai / Peace"),
    ("Heaven", "Earth"): (12, "Pi / Standstill"),
    ("Heaven", "Fire"): (13, "Tong Ren / Fellowship"),
    ("Fire", "Heaven"): (14, "Da You / Great Possession"),
    ("Earth", "Mountain"): (15, "Qian / Modesty"),
    ("Thunder", "Earth"): (16, "Yu / Enthusiasm"),
    ("Lake", "Thunder"): (17, "Sui / Following"),
    ("Mountain", "Wind"): (18, "Gu / Work on the Decayed"),
    ("Earth", "Lake"): (19, "Lin / Approach"),
    ("Wind", "Earth"): (20, "Guan / Contemplation"),
    ("Fire", "Thunder"): (21, "Shi He / Biting Through"),
    ("Mountain", "Fire"): (22, "Bi / Grace"),
    ("Mountain", "Earth"): (23, "Bo / Splitting Apart"),
    ("Earth", "Thunder"): (24, "Fu / Return"),
    ("Heaven", "Thunder"): (25, "Wu Wang / Innocence"),
    ("Mountain", "Heaven"): (26, "Da Chu / Great Taming"),
    ("Mountain", "Thunder"): (27, "Yi / Nourishment"),
    ("Lake", "Wind"): (28, "Da Guo / Great Preponderance"),
    ("Water", "Water"): (29, "Kan / The Abysmal"),
    ("Fire", "Fire"): (30, "Li / The Clinging"),
    ("Lake", "Mountain"): (31, "Xian / Influence"),
    ("Thunder", "Wind"): (32, "Heng / Duration"),
    ("Heaven", "Mountain"): (33, "Dun / Retreat"),
    ("Thunder", "Heaven"): (34, "Da Zhuang / Great Power"),
    ("Fire", "Earth"): (35, "Jin / Progress"),
    ("Earth", "Fire"): (36, "Ming Yi / Darkening of the Light"),
    ("Wind", "Fire"): (37, "Jia Ren / The Family"),
    ("Fire", "Lake"): (38, "Kui / Opposition"),
    ("Water", "Mountain"): (39, "Jian / Obstruction"),
    ("Thunder", "Water"): (40, "Jie / Deliverance"),
    ("Mountain", "Lake"): (41, "Sun / Decrease"),
    ("Wind", "Thunder"): (42, "Yi / Increase"),
    ("Lake", "Heaven"): (43, "Guai / Breakthrough"),
    ("Heaven", "Wind"): (44, "Gou / Coming to Meet"),
    ("Lake", "Earth"): (45, "Cui / Gathering Together"),
    ("Earth", "Wind"): (46, "Sheng / Pushing Upward"),
    ("Lake", "Water"): (47, "Kun / Oppression"),
    ("Water", "Wind"): (48, "Jing / The Well"),
    ("Lake", "Fire"): (49, "Ge / Revolution"),
    ("Fire", "Wind"): (50, "Ding / The Cauldron"),
    ("Thunder", "Thunder"): (51, "Zhen / The Arousing"),
    ("Mountain", "Mountain"): (52, "Gen / Keeping Still"),
    ("Wind", "Mountain"): (53, "Jian / Development"),
    ("Thunder", "Lake"): (54, "Gui Mei / Marrying Maiden"),
    ("Thunder", "Fire"): (55, "Feng / Abundance"),
    ("Fire", "Mountain"): (56, "Lu / The Wanderer"),
    ("Wind", "Wind"): (57, "Xun / The Gentle"),
    ("Lake", "Lake"): (58, "Dui / The Joyous"),
    ("Wind", "Water"): (59, "Huan / Dispersion"),
    ("Water", "Lake"): (60, "Jie / Limitation"),
    ("Wind", "Lake"): (61, "Zhong Fu / Inner Truth"),
    ("Thunder", "Mountain"): (62, "Xiao Guo / Small Preponderance"),
    ("Water", "Fire"): (63, "Ji Ji / After Completion"),
    ("Fire", "Water"): (64, "Wei Ji / Before Completion"),
}

HEXAGRAM_BY_BINARY = {
    TRIGRAM_BITS[lower] + TRIGRAM_BITS[upper]: {"number": number, "name": name, "upper": upper, "lower": lower}
    for (upper, lower), (number, name) in HEXAGRAMS.items()
}


# Classical judgment and line texts (周易卦爻辭), public domain,
# sourced from Chinese Wikisource (zh.wikisource.org/wiki/周易) and
# normalized for markup variants. Keyed by 6-bit binary, bottom line first.
HEXAGRAM_TEXTS = {
    "000000": {"judgment": "元亨。利牝馬之貞。", "lines": ["履霜，堅冰至。", "直方大，不習无不利。", "含章，可貞。或從王事，无成有終。", "括囊，无咎无譽。", "黃裳，元吉。", "龍戰于野，其血玄黃。", "利永貞。"], "line_labels": ["初六", "六二", "六三", "六四", "六五", "上六", "用六"]},
    "000001": {"judgment": "不利。有攸往。", "lines": ["剝牀以足，蔑貞凶。", "剝牀以辨，蔑貞凶。", "剝之，无咎。", "剝牀以膚，凶。", "貫魚，以宮人寵，无不利。", "碩果不食，君子得輿，小人剝廬。"], "line_labels": ["初六", "六二", "六三", "六四", "六五", "上九"]},
    "000010": {"judgment": "吉。原筮元永貞，无咎。不寧方來，後夫凶。", "lines": ["有孚，比之，无咎。有孚盈缶，終來有它，吉。", "比之自內，貞吉。", "比之匪人。", "外比之，貞吉。", "顯比。王用三驅，失前禽，邑人不誡，吉。", "比之无首，凶。"], "line_labels": ["初六", "六二", "六三", "六四", "九五", "上六"]},
    "000011": {"judgment": "盥而不荐，有孚顒若。", "lines": ["童觀，小人无咎，君子吝。", "窺觀，利女貞。", "觀我生，進退。", "觀國之光，利用賓于王。", "觀我生，君子无咎。", "觀其生，君子无咎。"], "line_labels": ["初六", "六二", "六三", "六四", "九五", "上九"]},
    "000100": {"judgment": "利建侯行師。", "lines": ["鳴豫，凶。", "介于石，不終日，貞吉。", "盱豫，悔。遲有悔。", "由豫，大有得。勿疑。朋盍簪。", "貞疾，恆不死。", "冥豫，成有渝，无咎。"], "line_labels": ["初六", "六二", "六三", "九四", "六五", "上六"]},
    "000101": {"judgment": "康侯用錫馬蕃庶，晝日三接。", "lines": ["晉如，摧如，貞吉。罔孚，裕无咎。", "晉如，愁如，貞吉。受茲介福，于其王母。", "眾允，悔亡。", "晉如鼫鼠，貞厲。", "悔亡，失得勿恤，往吉无不利。", "晉其角，維用伐邑，厲吉无咎，貞吝。"], "line_labels": ["初六", "六二", "六三", "九四", "六五", "上九"]},
    "000110": {"judgment": "亨。王假有廟，利見大人，亨。利貞。用大牲吉，利有攸往。", "lines": ["有孚不終，乃亂乃萃，若號一握為笑，勿恤，往无咎。", "引吉，无咎，孚乃利用禴。", "萃如，嗟如，无攸利，往无咎，小吝。", "大吉，无咎。", "萃有位，无咎。匪孚，元永貞，悔亡。", "齎咨涕洟，无咎。"], "line_labels": ["初六", "六二", "六三", "九四", "九五", "上六"]},
    "000111": {"judgment": "之匪人，不利君子貞，大往小來。", "lines": ["拔茅茹以其彙，貞吉。亨。", "包承，小人吉，大人否。亨。", "包羞。", "有命，无咎，疇離祉。", "休否，大人吉。其亡其亡，繫于苞桑。", "傾否，先否後喜。"], "line_labels": ["初六", "六二", "六三", "九四", "九五", "上九"]},
    "001000": {"judgment": "亨，君子有終。", "lines": ["謙謙君子，用涉大川，吉。", "鳴謙，貞吉。", "勞謙君子，有終吉。", "无不利，撝謙。", "不富，以其鄰，利用侵伐，无不利。", "鳴謙，利用行師，征邑國。"], "line_labels": ["初六", "六二", "九三", "六四", "六五", "上六"]},
    "001001": {"judgment": "艮其背，不獲其身，行其庭，不見其人，无咎。", "lines": ["艮其趾，无咎，利永貞。", "艮其腓，不拯其隨，其心不快。", "艮其限，列其夤，厲薰心。", "艮其身，无咎。", "艮其輔，言有序，悔亡。", "敦艮，吉。"], "line_labels": ["初六", "六二", "九三", "六四", "六五", "上九"]},
    "001010": {"judgment": "利西南，不利東北；利見大人，貞吉。", "lines": ["往蹇，來譽。", "王臣蹇蹇，匪躬之故。", "往蹇來反。", "往蹇來連。", "大蹇朋來。", "往蹇來碩，吉；利見大人。"], "line_labels": ["初六", "六二", "九三", "六四", "九五", "上六"]},
    "001011": {"judgment": "女歸吉，利貞。", "lines": ["鴻漸于干，小子厲，有言，无咎。", "鴻漸于磐，飲食衎衎，吉。", "鴻漸于陸，夫征不復，婦孕不育，凶；利禦寇。", "鴻漸于木，或得其桷，无咎。", "鴻漸于陵，婦三歲不孕，終莫之勝，吉。", "鴻漸于陸，其羽可用為儀，吉。"], "line_labels": ["初六", "六二", "九三", "六四", "九五", "上九"]},
    "001100": {"judgment": "亨。利貞。可小事，不可大事。飛鳥遺之音，不宜上宜下，大吉。", "lines": ["飛鳥以凶。", "過其祖，遇其妣；不及其君，遇其臣；无咎。", "弗過防之，從或戕之，凶。", "无咎，弗過遇之。往厲必戒，勿用永貞。", "密云不雨，自我西郊，公弋取彼在穴。", "弗遇過之，飛鳥離之，凶，是謂災眚。"], "line_labels": ["初六", "六二", "九三", "九四", "六五", "上六"]},
    "001101": {"judgment": "小亨，旅貞吉。", "lines": ["旅瑣瑣，斯其所取災。", "旅即次，懷其資，得童僕貞。", "旅焚其次，喪其童僕，貞厲。", "旅于處，得其資斧，我心不快。", "射雉一矢亡，終以譽命。", "鳥焚其巢，旅人先笑后號咷。喪牛于易，凶。"], "line_labels": ["初六", "六二", "九三", "九四", "六五", "上九"]},
    "001110": {"judgment": "亨。利貞。取女吉。", "lines": ["咸其拇。", "咸其腓，凶，居吉。", "咸其股，執其隨，往吝。", "貞吉悔亡，憧憧往來，朋從爾思。", "咸其脢，无悔。", "咸其輔，頰，舌。"], "line_labels": ["初六", "六二", "九三", "九四", "九五", "上六"]},
    "001111": {"judgment": "亨。小利貞。", "lines": ["遯尾，厲，勿用有攸往。", "執之用黃牛之革，莫之勝說。", "系遯，有疾厲，畜臣妾吉。", "好遯君子吉，小人否。", "嘉遯，貞吉。", "肥遯，无不利。"], "line_labels": ["初六", "六二", "九三", "九四", "九五", "上九"]},
    "010000": {"judgment": "貞丈人吉，无咎。", "lines": ["師出以律，否臧，凶。", "在師中吉，无咎；王三錫命。", "師或輿尸，凶。", "師左次，无咎。", "田有禽，利執言，无咎。長子帥師，弟子輿尸，貞凶。", "大君有命，開國承家，小人勿用。"], "line_labels": ["初六", "九二", "六三", "六四", "六五", "上六"]},
    "010001": {"judgment": "亨。匪我求童蒙，童蒙求我。初筮告，再三瀆，瀆則不告。利貞。", "lines": ["發蒙，利用刑人，用說桎梏，以往吝。", "包蒙吉，納婦吉，子克家。", "勿用取女，見金夫，不有躬，无攸利。", "困蒙，吝。", "童蒙，吉。", "擊蒙，不利為寇，利禦寇。"], "line_labels": ["初六", "九二", "六三", "六四", "六五", "上九"]},
    "010010": {"judgment": "有孚，維心亨。行有尚。", "lines": ["習坎，入于坎窞，凶。", "坎有險，求小得。", "來之坎坎，險且枕，入于坎窞，勿用。", "樽酒簋貳，用缶，納約自牖，終无咎。", "坎不盈，祗既平，无咎。", "係用徽纆，寘于叢棘，三歲不得，凶。"], "line_labels": ["初六", "九二", "六三", "六四", "九五", "上六"]},
    "010011": {"judgment": "亨。王假有廟，利涉大川，利貞。", "lines": ["用拯馬壯，吉。", "渙奔其机，悔亡。", "渙其躬，无悔。", "渙其群，元吉。渙有丘，匪夷所思。", "渙汗其大號，渙王居，无咎。", "渙其血，去逖出，无咎。"], "line_labels": ["初六", "九二", "六三", "六四", "九五", "上九"]},
    "010100": {"judgment": "利西南，无所往，其來復吉。有攸往，夙吉。", "lines": ["无咎。", "田獲三狐，得黃矢，貞吉。", "負且乘，致寇至，貞吝。", "解而拇，朋至斯孚。", "君子維有解，吉；有孚于小人。", "公用射隼，于高墉之上，獲之，无不利。"], "line_labels": ["初六", "九二", "六三", "九四", "六五", "上六"]},
    "010101": {"judgment": "亨。小狐汔濟，濡其尾，无攸利。", "lines": ["濡其尾，吝。", "曳其輪，貞吉。", "未濟，征凶，利涉大川。", "貞吉，悔亡，震用伐鬼方，三年有賞于大國。", "貞吉，无悔，君子之光，有孚，吉。", "有孚于飲酒，无咎，濡其首，有孚失是。"], "line_labels": ["初六", "九二", "六三", "九四", "六五", "上九"]},
    "010110": {"judgment": "亨，貞大人吉，无咎，有言不信。", "lines": ["臀困于株木，入于幽谷，三歲不覿。", "困于酒食，朱紱方來，利用亨祀，征凶，无咎。", "困于石，據于蒺藜，入于其宮，不見其妻，凶。", "來徐徐，困于金車，吝，有終。", "劓刖，困于赤紱，乃徐有說，利用祭祀。", "困于葛藟，于臲卼，曰動悔。有悔，征吉。"], "line_labels": ["初六", "九二", "六三", "九四", "九五", "上六"]},
    "010111": {"judgment": "有孚，窒，惕，中吉，終凶。利見大人，不利涉大川。", "lines": ["不永所事，小有言，終吉。", "不克訟，歸而逋，其邑人三百戶无眚。", "食舊德，貞厲，終吉。或從王事，无成。", "不克訟，復即命渝，安貞吉。", "訟，元吉。", "或錫之鞶帶，終朝三褫之。"], "line_labels": ["初六", "九二", "六三", "九四", "九五", "上九"]},
    "011000": {"judgment": "元亨，用見大人，勿恤，南征吉。", "lines": ["允升，大吉。", "孚乃利用禴，无咎。", "升虛邑。", "王用亨于岐山，吉无咎。", "貞吉，升階。", "冥升，利于不息之貞。"], "line_labels": ["初六", "九二", "九三", "六四", "六五", "上六"]},
    "011001": {"judgment": "元亨。利涉大川。先甲三日，後甲三日。", "lines": ["幹父之蠱，有子考，无咎，厲終吉。", "幹母之蠱，不可貞。", "幹父之蠱，小有悔，无大咎。", "裕父之蠱，往見吝。", "幹父之蠱，用譽。", "不事王侯，高尚其事。"], "line_labels": ["初六", "九二", "九三", "六四", "六五", "上九"]},
    "011010": {"judgment": "改邑不改井，无喪无得，往來井井。汔至亦未繘井。羸其瓶，凶。", "lines": ["井泥不食，舊井无禽。", "井谷射鮒，瓮敝漏。", "井渫不食，為我心惻，可用汲，王明，并受其福。", "井甃，无咎。", "井冽，寒泉食。", "井收勿幕，有孚元吉。"], "line_labels": ["初六", "九二", "九三", "六四", "九五", "上六"]},
    "011011": {"judgment": "小亨。利有攸往。利見大人。", "lines": ["進退，利武人之貞。", "巽在牀下，用史巫紛若，吉无咎。", "頻巽，吝。", "悔亡，田獲三品。", "貞吉悔亡，无不利。无初有終，先庚三日，后庚三日，吉。", "巽在牀下，喪其資斧，貞凶。"], "line_labels": ["初六", "九二", "九三", "六四", "九五", "上九"]},
    "011100": {"judgment": "亨，无咎。利貞，利有攸往。", "lines": ["浚恆，貞凶，无攸利。", "悔亡。", "不恆其德，或承之羞，貞吝。", "田无禽。", "恆其德，貞，婦人吉，夫子凶。", "振恆，凶。"], "line_labels": ["初六", "九二", "九三", "九四", "六五", "上六"]},
    "011101": {"judgment": "元吉，亨。", "lines": ["鼎顛趾，利出否，得妾以其子，无咎。", "鼎有實，我仇有疾，不我能即，吉。", "鼎耳革，其行塞，雉膏不食，方雨虧悔，終吉。", "鼎折足，覆公餗，其形渥，凶。", "鼎黃耳金鉉，利貞。", "鼎玉鉉，大吉，无不利。"], "line_labels": ["初六", "九二", "九三", "九四", "六五", "上九"]},
    "011110": {"judgment": "棟橈，利有攸往，亨。", "lines": ["藉用白茅，无咎。", "枯楊生稊，老夫得其女妻，无不利。", "棟橈，凶。", "棟隆，吉。有它吝。", "枯楊生華，老婦得其士夫，无咎无譽。", "過涉滅頂，凶，无咎。"], "line_labels": ["初六", "九二", "九三", "九四", "九五", "上六"]},
    "011111": {"judgment": "女壯，勿用取女。", "lines": ["系于金柅，貞吉，有攸往，見凶，羸豕孚踟躅。", "包有魚，无咎，不利賓。", "臀无膚，其行次且，厲，无大咎。", "包无魚，起凶。", "以杞包瓜，含章，有隕自天。", "姤其角，吝，无咎。"], "line_labels": ["初六", "九二", "九三", "九四", "九五", "上九"]},
    "100000": {"judgment": "亨。出入无疾，朋來无咎。反復其道，七日來復，利有攸往。", "lines": ["不復遠，无袛悔，元吉。", "休復，吉。", "頻復，厲无咎。", "中行獨復。", "敦復，无悔。", "迷復，凶，有災眚。用行師，終有大敗，以其國君，凶；至于十年，不克征。"], "line_labels": ["初九", "六二", "六三", "六四", "六五", "上六"]},
    "100001": {"judgment": "貞吉。觀頤，自求口實。", "lines": ["舍爾靈龜，觀我朵頤，凶。", "顛頤，拂經，于丘頤，征凶。", "拂頤，貞凶，十年勿用，无攸利。", "顛頤吉，虎視眈眈，其欲逐逐，无咎。", "拂經，居貞吉，不可涉大川。", "由頤，厲吉，利涉大川。"], "line_labels": ["初九", "六二", "六三", "六四", "六五", "上九"]},
    "100010": {"judgment": "元亨，利貞。勿用有攸往，利建侯。", "lines": ["磐桓，利居貞，利建侯。", "屯如邅如，乘馬班如，匪寇婚媾，女子貞不字，十年乃字。", "即鹿无虞，惟入于林中，君子幾不如舍，往吝。", "乘馬班如，求婚媾，往，吉无不利。", "屯其膏；小貞吉，大貞凶。", "乘馬班如，泣血漣如。"], "line_labels": ["初九", "六二", "六三", "六四", "九五", "上六"]},
    "100011": {"judgment": "利有攸往。利涉大川。", "lines": ["利用為大作，元吉，无咎。", "或益之，十朋之龜弗克違，永貞吉。王用享于帝，吉。", "益之用凶事，无咎。有孚中行，告公用圭。", "中行，告公從。利用為依遷國。", "有孚惠心，勿問元吉。有孚惠我德。", "莫益之，或擊之，立心勿恆，凶。"], "line_labels": ["初九", "六二", "六三", "六四", "九五", "上九"]},
    "100100": {"judgment": "亨。震來虩虩，笑言啞啞。震驚百里，不喪匕鬯。", "lines": ["震來虩虩，后笑言啞啞，吉。", "震來厲，億喪貝，躋于九陵，勿逐，七日得。", "震蘇蘇，震行无眚。", "震遂泥。", "震往來厲，億无喪，有事。", "震索索，視矍矍，征凶。震不于其躬，于其鄰，无咎。婚媾有言。"], "line_labels": ["初九", "六二", "六三", "九四", "六五", "上六"]},
    "100101": {"judgment": "亨。利用獄。", "lines": ["屨校滅趾，无咎。", "噬膚滅鼻，无咎。", "噬臘肉，遇毒；小吝，无咎。", "噬乾胏，得金矢，利艱貞，吉。", "噬乾肉，得黃金，貞厲，无咎。", "何校滅耳，凶。"], "line_labels": ["初九", "六二", "六三", "九四", "六五", "上九"]},
    "100110": {"judgment": "元亨。利貞。无咎。", "lines": ["官有渝，貞吉。出門交有功。", "系小子，失丈夫。", "系丈夫，失小子。隨，有求得利，居貞。", "隨有獲，貞凶。有孚在道，以明，何咎。", "孚于嘉，吉。", "拘系之，乃從維之。王用亨于西山。"], "line_labels": ["初九", "六二", "六三", "九四", "九五", "上六"]},
    "100111": {"judgment": "元亨。利貞。其匪正有眚，不利有攸往。", "lines": ["无妄，往吉。", "不耕穫，不菑畬，則利有攸往。", "无妄之災，或系之牛，行人之得，邑人之災。", "可貞，无咎。", "无妄之疾，勿藥有喜。", "无妄，行有眚，无攸利。"], "line_labels": ["初九", "六二", "六三", "九四", "九五", "上九"]},
    "101000": {"judgment": "利艱貞。", "lines": ["明夷于飛，垂其翼。君子于行，三日不食，有攸往，主人有言。", "明夷，夷于左股，用拯馬壯，吉。", "明夷于南狩，得其大首，不可疾貞。", "入于左腹，獲明夷之心，于出門庭。", "箕子之明夷，利貞。", "不明晦，初登于天，后入于地。"], "line_labels": ["初九", "六二", "九三", "六四", "六五", "上六"]},
    "101001": {"judgment": "亨。小利有攸往。", "lines": ["賁其趾，舍車而徒。", "賁其須。", "賁如濡如，永貞吉。", "賁如皤如，白馬翰如，匪寇婚媾。", "賁於丘園，束帛戔戔，吝，終吉。", "白賁，无咎。"], "line_labels": ["初九", "六二", "九三", "六四", "六五", "上九"]},
    "101010": {"judgment": "亨小。利貞。初吉終亂。", "lines": ["曳其輪，濡其尾，无咎。", "婦喪其茀，勿逐，七日得。", "高宗伐鬼方，三年克之，小人勿用。", "繻有衣袽，終日戒。", "東鄰殺牛，不如西鄰之禴祭，實受其福。", "濡其首，厲。"], "line_labels": ["初九", "六二", "九三", "六四", "九五", "上六"]},
    "101011": {"judgment": "利女貞。", "lines": ["閑有家，悔亡。", "无攸遂，在中饋，貞吉。", "家人嗃嗃，悔厲吉；婦子嘻嘻，終吝。", "富家，大吉。", "王假有家，勿恤。吉。", "有孚威如，終吉。"], "line_labels": ["初九", "六二", "九三", "六四", "九五", "上九"]},
    "101100": {"judgment": "亨。王假之，勿憂，宜日中。", "lines": ["遇其配主，雖旬无咎，往有尚。", "豐其蔀，日中見斗，往得疑疾，有孚發若，吉。", "豐其沛，日中見沫，折其右肱，无咎。", "豐其蔀，日中見斗，遇其夷主，吉。", "來章，有慶譽，吉。", "豐其屋，蔀其家，窺其戶，闃其无人，三歲不觌，凶。"], "line_labels": ["初九", "六二", "九三", "九四", "六五", "上六"]},
    "101101": {"judgment": "利貞。亨。畜牝牛，吉。", "lines": ["履錯然，敬之无咎。", "黃離，元吉。", "日昃之離，不鼓缶而歌，則大耋之嗟，凶。", "突如其來如，焚如，死如，棄如。", "出涕沱若，戚嗟若，吉。", "王用出征，有嘉折首，獲匪其醜，无咎。"], "line_labels": ["初九", "六二", "九三", "九四", "六五", "上九"]},
    "101110": {"judgment": "巳日乃孚，元亨。利貞。悔亡。", "lines": ["鞏用黃牛之革。", "巳日乃革之，征吉，无咎。", "征凶，貞厲，革言三就，有孚。", "悔亡，有孚改命，吉。", "大人虎變，未占有孚。", "君子豹變，小人革面，征凶，居貞吉。"], "line_labels": ["初九", "六二", "九三", "九四", "九五", "上六"]},
    "101111": {"judgment": "于野，亨。 利涉大川，利君子貞。", "lines": ["同人于門，無咎。", "同人于宗，吝。", "伏戎于莽，升其高陵，三歲不興。", "乘其墉，弗克，攻吉。", "同人，先號啕而后笑。大師克相遇。", "同人于郊，無悔。"], "line_labels": ["初九", "六二", "九三", "九四", "九五", "上九"]},
    "110000": {"judgment": "元亨。利貞。至于八月有凶。", "lines": ["咸臨，貞吉。", "咸臨，吉无不利。", "甘臨，无攸利。既憂之，无咎。", "至臨，无咎。", "知臨，大君之宜，吉。", "敦臨，吉无咎。"], "line_labels": ["初九", "九二", "六三", "六四", "六五", "上六"]},
    "110001": {"judgment": "有孚，元吉。无咎，可貞，利有攸往。曷之用？二簋可用享。", "lines": ["已事遄往，无咎，酌損之。", "利貞，征凶，弗損益之。", "三人行，則損一人；一人行，則得其友。", "損其疾，使遄有喜，无咎。", "或益之，十朋之龜弗克違，元吉。", "弗損益之，无咎，貞吉，利有攸往，得臣无家。"], "line_labels": ["初九", "九二", "六三", "六四", "六五", "上九"]},
    "110010": {"judgment": "亨。苦節不可貞。", "lines": ["不出戶庭，无咎。", "不出門庭，凶。", "不節若，則嗟若，无咎。", "安節，亨。", "甘節，吉；往有尚。", "苦節，貞凶，悔亡。"], "line_labels": ["初九", "九二", "六三", "六四", "九五", "上六"]},
    "110011": {"judgment": "豚魚吉，利涉大川，利貞。", "lines": ["虞吉，有他不燕。", "鳴鶴在陰，其子和之，我有好爵，吾與爾靡之。", "得敵，或鼓或罷，或泣或歌。", "月几望，馬匹亡，无咎。", "有孚攣如，无咎。", "翰音登于天，貞凶。"], "line_labels": ["初九", "九二", "六三", "六四", "九五", "上九"]},
    "110100": {"judgment": "征凶，无攸利。", "lines": ["歸妹以娣，跛能履，征吉。", "眇能視，利幽人之貞。", "歸妹以須，反歸以娣。", "歸妹愆期，遲歸有時。", "帝乙歸妹，其君之袂，不如其娣之袂良，月幾望，吉。", "女承筐无實，士刲羊无血，无攸利。"], "line_labels": ["初九", "九二", "六三", "九四", "六五", "上六"]},
    "110101": {"judgment": "小事吉。", "lines": ["悔亡，喪馬勿逐，自復；見惡人无咎。", "遇主于巷，无咎。", "見輿曳，其牛掣，其人天且劓，无初有終。", "睽孤，遇元夫，交孚，厲无咎。", "悔亡，厥宗噬膚，往何咎。", "睽孤， 見豕負涂，載鬼一車， 先張之弧，后說之弧，匪寇婚媾，往遇雨則吉。"], "line_labels": ["初九", "九二", "六三", "九四", "六五", "上九"]},
    "110110": {"judgment": "亨。利貞。", "lines": ["和兌，吉。", "孚兌，吉，悔亡。", "來兌，凶。", "商兌，未寧，介疾有喜。", "孚于剝，有厲。", "引兌。"], "line_labels": ["初九", "九二", "六三", "九四", "九五", "上六"]},
    "110111": {"judgment": "虎尾，不咥人，亨。", "lines": ["素履，往无咎。", "履道坦坦，幽人貞吉。", "眇能視，跛能履，履虎尾，咥人，凶。武人為于大君。", "履虎尾，愬愬終吉。", "夬履，貞厲。", "視履考祥，其旋元吉。"], "line_labels": ["初九", "九二", "六三", "九四", "九五", "上九"]},
    "111000": {"judgment": "小往大來，吉亨。", "lines": ["拔茅茹以其彙，征吉。", "包荒。用馮河，不遐遺；朋亡。得尚于中行。", "无平不陂，无往不復，艱貞无咎。勿恤其孚，于食有福。", "翩翩，不富以其鄰；不戒以孚。", "帝乙歸妹，以祉，元吉。", "城復于隍，勿用師，自邑告命，貞吝。"], "line_labels": ["初九", "九二", "九三", "六四", "六五", "上六"]},
    "111001": {"judgment": "利貞，不家食吉，利涉大川。", "lines": ["有厲利已。", "輿說輹。", "良馬逐，利艱貞。曰閑輿衛，利有攸往。", "童牛之牿，元吉。", "豶豕之牙，吉。", "何天之衢，亨。"], "line_labels": ["初九", "九二", "九三", "六四", "六五", "上九"]},
    "111010": {"judgment": "有孚，光亨。貞吉，利涉大川。", "lines": ["需于郊，利用恆，无咎。", "需于沙，小有言，終吉。", "需于泥，致寇至。", "需于血，出自穴。", "需于酒食，貞吉。", "入于穴，有不速之客三人來，敬之終吉。"], "line_labels": ["初九", "九二", "九三", "六四", "九五", "上六"]},
    "111011": {"judgment": "亨。密雲不雨，自我西郊。", "lines": ["復自道，何其咎，吉。", "牽復，吉。", "輿說輻，夫妻反目。", "有孚，血去惕出，无咎。", "有孚攣如，富以其鄰。", "既雨既處，尚德載，婦貞厲，月幾望，君子征凶。"], "line_labels": ["初九", "九二", "九三", "六四", "九五", "上九"]},
    "111100": {"judgment": "利貞。", "lines": ["壯于趾，征凶，有孚。", "貞吉。", "小人用壯，君子用罔，貞厲。羝羊觸藩，羸其角。", "貞吉悔亡，藩決不羸，壯于大輿之輹。", "喪羊于易，无悔。", "羝羊觸藩，不能退，不能遂，无攸利，艱則吉。"], "line_labels": ["初九", "九二", "九三", "九四", "六五", "上六"]},
    "111101": {"judgment": "元亨。", "lines": ["无交害，匪咎，艱則无咎。", "大車以載，有攸往，无咎。", "公用亨于天子，小人弗克。", "匪其彭，无咎。", "厥孚交如，威如；吉。", "自天佑之，吉无不利。"], "line_labels": ["初九", "九二", "九三", "九四", "六五", "上九"]},
    "111110": {"judgment": "揚于王庭，孚號，有厲，告自邑，不利即戎，利有攸往。", "lines": ["壯于前趾，往不勝為咎。", "惕號，莫夜有戎，勿恤。", "壯于頄，有凶。君子夬夬，獨行遇雨，若濡有慍，无咎。", "臀无膚，其行次且。牽羊悔亡，聞言不信。", "莧陸夬夬，中行无咎。", "无號，終有凶。"], "line_labels": ["初九", "九二", "九三", "九四", "九五", "上六"]},
    "111111": {"judgment": "元亨。利貞。", "lines": ["潛龍勿用。", "見龍在田，利見大人。", "君子終日乾乾，夕惕若；厲，无咎。", "或躍在淵，无咎。", "飛龍在天，利見大人。", "亢龍，有悔。", "見羣龍无首，吉。"], "line_labels": ["初九", "九二", "九三", "九四", "九五", "上九", "用九"]},
}


def make_rng(seed: str | None) -> random.Random | random.SystemRandom:
    if seed is not None:
        return random.Random(seed)
    return random.SystemRandom()


def coin_line_record(index: int, rng: random.Random | random.SystemRandom) -> dict[str, Any]:
    tosses = [rng.choice(["heads", "tails"]) for _ in range(3)]
    values = [3 if toss == "heads" else 2 for toss in tosses]
    record = line_record(index, sum(values))
    record["coin_tosses"] = tosses
    record["coin_values"] = values
    return record


def yarrow_line_value(rng: random.Random | random.SystemRandom) -> int:
    roll = rng.randrange(16)
    if roll == 0:
        return 6
    if roll <= 5:
        return 7
    if roll <= 12:
        return 8
    return 9


def parse_manual_lines(raw: str) -> list[int]:
    values = [int(part.strip()) for part in raw.split(",") if part.strip()]
    if len(values) != 6:
        raise ValueError("--lines must contain exactly six comma-separated values")
    if any(value not in [6, 7, 8, 9] for value in values):
        raise ValueError("line values must be 6, 7, 8, or 9")
    return values


def line_record(index: int, value: int) -> dict[str, Any]:
    labels = {
        6: ("old yin", "yin", True),
        7: ("young yang", "yang", False),
        8: ("young yin", "yin", False),
        9: ("old yang", "yang", True),
    }
    line_type, polarity, changing = labels[value]
    return {
        "line": index,
        "value": value,
        "type": line_type,
        "polarity": polarity,
        "changing": changing,
    }


def hexagram_for_binary(binary: str, with_texts: bool = True) -> dict[str, Any]:
    data = HEXAGRAM_BY_BINARY[binary]
    result = {
        "number": data["number"],
        "name": data["name"],
        "binary": binary,
        "upper_trigram": data["upper"],
        "lower_trigram": data["lower"],
    }
    if with_texts:
        texts = HEXAGRAM_TEXTS[binary]
        result["texts"] = {
            "judgment": texts["judgment"],
            "line_labels": texts["line_labels"],
            "line_texts": texts["lines"],
            "source": "Zhou Yi (public domain), via Chinese Wikisource",
        }
    return result


def cast(method: str, seed: str | None, manual_lines: str | None) -> dict[str, Any]:
    requested_method = method
    warning = None
    if method == "random":
        method = "coins"
        warning = "Compatibility alias: --method random now uses the three-coin method. Use --method coins or --method yarrow for explicit traditional casting."

    if method == "manual":
        if not manual_lines:
            raise ValueError("--lines is required for manual casts")
        values = parse_manual_lines(manual_lines)
        randomness = "manual"
        lines = [line_record(index, value) for index, value in enumerate(values, start=1)]
        method_details = {"name": "manual", "line_order": "bottom-to-top"}
        line_probabilities = {}
    elif method == "yarrow":
        rng = make_rng(seed)
        values = [yarrow_line_value(rng) for _ in range(6)]
        randomness = "seeded" if seed is not None else "system"
        lines = [line_record(index, value) for index, value in enumerate(values, start=1)]
        method_details = {
            "name": "digital yarrow equivalent",
            "probability_model": "digital-yarrow-equivalent",
            "note": "Uses the traditional yarrow-stalk line probability distribution without simulating physical stalk manipulation.",
        }
        line_probabilities = {"6": "1/16", "7": "5/16", "8": "7/16", "9": "3/16"}
    else:
        rng = make_rng(seed)
        lines = [coin_line_record(index, rng) for index in range(1, 7)]
        values = [line["value"] for line in lines]
        randomness = "seeded" if seed is not None else "system"
        method_details = {
            "name": "three coins",
            "coin_value_map": {"heads": 3, "tails": 2},
            "line_order": "bottom-to-top",
        }
        line_probabilities = {"6": "1/8", "7": "3/8", "8": "3/8", "9": "1/8"}

    primary_bits = "".join("1" if value in [7, 9] else "0" for value in values)
    resulting_bits = "".join(
        "0" if value == 9 else "1" if value in (6, 7) else "0"
        for value in values
    )
    changing_lines = [line["line"] for line in lines if line["changing"]]
    primary_texts = HEXAGRAM_TEXTS[primary_bits]
    changing_line_texts = [
        {
            "line": line_no,
            "label": primary_texts["line_labels"][line_no - 1],
            "text": primary_texts["lines"][line_no - 1],
        }
        for line_no in changing_lines
    ]
    result = {
        "system": "iching",
        "method": method,
        "requested_method": requested_method,
        "randomness": randomness,
        "line_order": "bottom-to-top",
        "method_details": method_details,
        "line_probabilities": line_probabilities,
        "lines": lines,
        "changing_lines": changing_lines,
        "changing_line_texts": changing_line_texts,
        "primary_hexagram": hexagram_for_binary(primary_bits),
        "resulting_hexagram": hexagram_for_binary(resulting_bits),
    }
    if warning:
        result["warning"] = warning
    return result


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Cast an I Ching hexagram for AI agent interpretation.")
    parser.add_argument("--method", choices=["random", "coins", "yarrow", "manual"], default="coins")
    parser.add_argument("--seed", help="Optional deterministic seed for tests and reproducible demos.")
    parser.add_argument("--lines", help="Manual bottom-to-top line values, for example: 6,7,8,9,7,8")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    result = cast(args.method, args.seed, args.lines)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0
