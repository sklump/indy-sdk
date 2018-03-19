import json

import pytest
from typing import Optional

from indy import anoncreds
from tests.conftest import path_home as x_path_home, pool_name as x_pool_name, wallet_name as x_wallet_name, \
    wallet_type as x_wallet_type, wallet_runtime_config as x_wallet_runtime_config, \
    xwallet_cleanup as x_xwallet_cleanup, wallet_handle_cleanup as x_wallet_handle_cleanup, \
    wallet_handle as x_wallet_handle, \
    xwallet as x_xwallet


@pytest.fixture(scope="module")
def path_home():
    # noinspection PyTypeChecker
    for i in x_path_home():
        yield i


@pytest.fixture(scope="module")
def pool_name():
    return x_pool_name()


@pytest.fixture(scope="module")
def wallet_name():
    return x_wallet_name()


@pytest.fixture(scope="module")
def wallet_type():
    return x_wallet_type()


@pytest.fixture(scope="module")
def wallet_runtime_config():
    return x_wallet_runtime_config()


@pytest.fixture(scope="module")
def xwallet_cleanup():
    return x_xwallet_cleanup()


# noinspection PyUnusedLocal
@pytest.fixture(scope="module")
def xwallet(event_loop, pool_name, wallet_name, wallet_type, xwallet_cleanup, path_home):
    xwallet_gen = x_xwallet(event_loop, pool_name, wallet_name, wallet_type, xwallet_cleanup, path_home, None)
    yield next(xwallet_gen)
    next(xwallet_gen)


@pytest.fixture(scope="module")
def wallet_handle_cleanup():
    return x_wallet_handle_cleanup()


@pytest.fixture(scope="module")
def wallet_handle(event_loop, wallet_name, xwallet, wallet_runtime_config, wallet_handle_cleanup):
    wallet_handle_gen = \
        x_wallet_handle(event_loop, wallet_name, xwallet, wallet_runtime_config, None, wallet_handle_cleanup)
    yield next(wallet_handle_gen)
    next(wallet_handle_gen)


@pytest.fixture(scope="module")
def default_cred_def_config():
    return json.dumps({"support_revocation": False})


@pytest.fixture(scope="module")
def tag():
    return "tag1"


@pytest.fixture(scope="module")
def id_credential_1():
    return "id_credential_1"


@pytest.fixture(scope="module")
def id_credential_2():
    return "id_credential_2"


@pytest.fixture(scope="module")
def id_credential_3():
    return "id_credential_3"


@pytest.fixture(scope="module")
def issuer_did():
    return "NcYxiDXkpYi6ov5FcYDi1e"


@pytest.fixture(scope="module")
def issuer_did_2():
    return "VsKV7grR1BUE29mG2Fm2kX"


@pytest.fixture(scope="module")
def prover_did():
    return "CnEDk9HrMnmiHXEV1WFgbVCRteYnPqsJwrTdcZaNhFVW"


def build_id(identifier: str, marker: str, related_entity_id: Optional[str], word1: str, word2: str):
    delimiter = ":"
    related_entity_id = related_entity_id + delimiter if related_entity_id else ""
    return identifier + delimiter + marker + delimiter + related_entity_id + word1 + delimiter + word2


@pytest.fixture(scope="module")
def gvt_schema_id(issuer_did):
    return build_id(issuer_did, "2", None, "gvt", "1.0")


@pytest.fixture(scope="module")
def gvt_schema(gvt_schema_id):
    return {
        "id": gvt_schema_id,
        "name": "gvt",
        "version": "1.0",
        "attrNames": ["name", "age", "sex", "height"]
    }


@pytest.fixture(scope="module")
def gvt_schema_json(gvt_schema):
    return json.dumps(gvt_schema)


@pytest.fixture(scope="module")
def xyz_schema_id(issuer_did):
    return build_id(issuer_did, "2", None, "xyz", "1.0")


@pytest.fixture(scope="module")
def xyz_schema(xyz_schema_id):
    return {
        "id": xyz_schema_id,
        "name": "xyz",
        "version": "1.0",
        "attrNames": ["status", "period"]
    }


@pytest.fixture(scope="module")
def xyz_schema_json(issuer_did, xyz_schema_id, xyz_schema):
    return json.dumps(xyz_schema)


@pytest.fixture(scope="module")
def master_secret_id():
    return "common_master_secret_name"


@pytest.fixture(scope="module")
def issuer_1_gvt_cred_def_id(issuer_did, gvt_schema_id):
    return build_id(issuer_did, "3", gvt_schema_id, "CL", "tag1")


@pytest.fixture(scope="module")
def issuer_1_xyz_cred_def_id(issuer_did, xyz_schema_id):
    return build_id(issuer_did, "3", xyz_schema_id, "CL", "tag1")


@pytest.fixture(scope="module")
def issuer_2_gvt_cred_def_id(issuer_did_2, gvt_schema_id):
    return build_id(issuer_did_2, "3", gvt_schema_id, "CL", "tag1")


def credential_offer(credential_def_id):
    return {
        "credential_def_id": credential_def_id,
        "nonce": "12345678",
        "key_correctness_proof": {
            "c": "40983841062403114696351105468714473190092945361781922980284036284848255102181",
            "xz_cap": "213464720484089744362618540118202909431724596227070046572799595772146912256777238162172299903278411669692103853805864530643873553457214761106883317761027120427539370942370962393243000202519433219346910021513926418330149853541417254168868250711855156634731074143905917765057402152157911116556639972831731251935718700937677764992720913700241472793061399051130783380568753128719906986229399266611916274676591429895036623790763995576609783339973743504299970516925347817430071017432740932267531399950884977365109931994767334355518355993866340663897276958741231492087880026463329993917787126111107043213858416969200146216919724481899757743335320111464498989394895406342200088098092363803780335427461",
            "xr_cap": {
                "age": "428551817403717345496666225339792093375807052545681523267375890344316772830711607454203456132869878139513849454441680693213618371219989695825485734499740269394536720808195352535836241683894046154422601982139187282874298237872016126349886775459552952772019552508536658271791921689339332976876098011786609958781975486656330572741194023204426484952261795227021910523213710060753808292174119734371160619117183552237714301799404966964550022274275304553920529452381773256570920044318126774874528737572897410668952113510485617038975261423255802900402119311766709164727308287389090038205944899002702399329914812218958604251060872288309671952489910694000990814697006984351987506978581894973799401592211",
                "height": "411657369769012290217285704283327594441623457932786578784814099069982464122634859546109989278195207865751652851745795318226450710002590664034182094394469565119510105316695655956892227633500179147318075067585551834678079812461536830790528252558459232505987954022333485123452283103020768033499524916346016600527748463901810773406682862302906632677327131603416116045070433377354243916235831969703006718595171020843309342047669615896623593427073236313132690348520294916012881797187163597866196204765064323603066770657621979137899593499157032831120638301825327588467780000638198687916279993936278677557249905181200340769464532921226462449219936857163316761986408035441733035901688059567989300117882",
                "name": "869322975653258356083915983990526979728408630010817458571291042713509811788475578121058954003892631131467356704604351238331780894204614591041662184716582274656810743747383953498817535302551304877321807454020020152874312640585570851593902460677745364557958108957714916300524302083561141490749493731078047092029485764829854763907822331747337420362381448975375124969403844387156269077805007874513313426920627145892677170274354768722781701010279364942880411045002631531693007422568259696565436694533169879230288912084861052431355880089929921941631003274141039364415665970063262534617675591334457554707139889594182371941548502441982219614399925468254660740292400093419154694726435630358592702798293",
                "sex": "80391464088175985479491145491149691676821702211894975540979533937774408491785219834122762944971811095537317848654416410580026667952335862665033546961195841179049138780634877378888139872391903804566992942049889566118414459535461354834916790111149556147862372720479995171424595620702416860508557772658191427975040372006893431243929350584258325646184152369207604974849840003307909256680303811690743921237117427932325288396536300357224457903672928805464748280413883820982138162562660615091490216949908906589977916965927522227509078411025411863914347809289131586019476288990589861921562466467956967324009607175203666778312423056471533641756179235960697838324279027572094105302470967687825859737087"
            }
        }
    }


@pytest.fixture(scope="module")
def issuer_1_gvt_cred_offer(issuer_1_gvt_cred_def_id):
    return credential_offer(issuer_1_gvt_cred_def_id)


@pytest.fixture(scope="module")
def issuer_1_gvt_cred_offer_json(credential_offer_issuer_1_schema_1):
    return json.dumps(credential_offer_issuer_1_schema_1)


@pytest.fixture(scope="module")
def issuer_1_xyz_cred_offer_json(issuer_1_xyz_cred_def_id):
    return credential_offer(issuer_1_xyz_cred_def_id)


@pytest.fixture(scope="module")
def issuer_1_xyz_cred_offer_json(credential_offer_issuer_1_schema_2):
    return json.dumps(credential_offer_issuer_1_schema_2)


@pytest.fixture(scope="module")
def issuer_2_gvt_cred_offer(issuer_2_gvt_cred_def_id):
    return credential_offer(issuer_2_gvt_cred_def_id)


@pytest.fixture(scope="module")
def issuer_2_gvt_cred_offer_json(credential_offer_issuer_2_schema_1):
    return json.dumps(credential_offer_issuer_2_schema_1)


@pytest.fixture(scope="module")
def gvt_cred_values():
    return {
        "sex": {
            "raw": "male", "encoded": "5944657099558967239210949258394887428692050081607692519917050011144233115103"},
        "name": {"raw": "Alex", "encoded": "1139481716457488690172217916278103335"},
        "height": {"raw": "175", "encoded": "175"},
        "age": {"raw": "28", "encoded": "28"}
    }


@pytest.fixture(scope="module")
def gvt_cred_values_json(gvt_cred_values):
    return json.dumps(gvt_cred_values)


@pytest.fixture(scope="module")
def gvt_cred_values_2():
    return {
        "sex": {
            "raw": "male", "encoded": "2142657394558967239210949258394838228692050081607692519917028371144233115103"},
        "name": {"raw": "Alexander", "encoded": "21332817548165488690172217217278169335"},
        "height": {"raw": "170", "encoded": "170"},
        "age": {"raw": "28", "encoded": "28"}
    }


@pytest.fixture(scope="module")
def gvt_2_cred_values_json(gvt_cred_values_2):
    return json.dumps(gvt_cred_values_2)


@pytest.fixture(scope="module")
def xyz_cred_values():
    return {
        "status": {"raw": "partial", "encoded": "51792877103171595686471452153480627530895"},
        "period": {"raw": "8", "encoded": "8"}
    }


@pytest.fixture(scope="module")
def xyz_cred_values_json(xyz_cred_values):
    return json.dumps(xyz_cred_values)


@pytest.fixture(scope="module")
def predicate_value():
    return 18


@pytest.fixture(scope="module")
def proof_req(predicate_value):
    return {
        "nonce": "123432421212",
        "name": "proof_req_1",
        "version": "0.1",
        "requested_attrs": {
            "attr1_referent": {"name": "name"}
        },
        "requested_predicates": {
            "predicate1_referent": {
                "attr_name": "age",
                "p_type": ">=",
                "value": predicate_value
            }
        }
    }


@pytest.fixture(scope="module")
def proof_req_json(proof_req):
    return json.dumps(proof_req)


@pytest.fixture(scope="module")
def credential_def(gvt_schema_id, issuer_1_gvt_cred_def_id):
    return {
        "id": issuer_1_gvt_cred_def_id,
        "schemaId": gvt_schema_id,
        "type": "CL",
        "tag": "TAG_1",
        "value": {
            "primary": {
                "n": "94759924268422840873493186881483285628376767714620627055233230078254863658476446487556117977593248501523199451418346650764648601684276437772084327637083000213497377603495837360299641742248892290843802071224822481683143989223918276185323177379400413928352871249494885563503003839960930062341074783742062464846448855510814252519824733234277681749977392772900212293652238651538092092030867161752390937372967233462027620699196724949212432236376627703446877808405786247217818975482797381180714523093913559060716447170497587855871901716892114835713057965087473682457896508094049813280368069805661739141591558517233009123957",
                "s": "3589207374161609293256840431433442367968556468254553005135697551692970564853243905310862234226531556373974144223993822323573625466428920716249949819187529684239371465431718456502388533731367046146704547241076626874082510133130124364613881638153345624380195335138152993132904167470515345775215584510356780117368593105284564368954871044494967246738070895990267205643985529060025311535539534155086912661927003271053443110788963970349858709526217650537936123121324492871282397691771309596632805099306241616501610166028401599243350835158479028294769235556557248339060399322556412171888114265194198405765574333538019124846",
                "rms": "57150374376895616256492932008792437185713712934712117819417607831438470701645904776986426606717466732609284990796923331049549544903261623636958698296956103821068569714644825742048584174696465882627177060166162341112552851798863535031243458188976013190131935905789786836375734914391914349188643340535242562896244661798678234667651641013894284156416773868299435641426810968290584996112925365638881750944407842890875840705650290814965768221299488400872767679122749231050406680432079499973527780212310700022178178822528199576164498116369689770884051691678056831493476045361227274839673581033532995523269047577973637307053",
                "r": {
                    "age": "94304485801056920773231824603827244147437820123357994068540328541540143488826838939836897544389872126768239056314698953816072289663428273075648246498659039419931054256171488371404693243192741923382499918184822032756852725234903892700640856294525441486319095181804549558538523888770076173572615957495813339649470619615099181648313548341951673407624414494737018574238782648822189142664108450534642272145962844003886059737965854042074083374478426875684184904488545593139633653407062308621502392373426120986761417580127895634822264744063122368296502161439648408926687989964483291459079738447940651025900007635890755686910",
                    "sex": "29253365609829921413347591854991689007250272038394995372767401325848195298844802462252851926995846503104090589196060683329875231216529049681648909174047403783834364995363938741001507091534282239210301727771803410513303526378812888571225762557471133950393342500638551458868147905023198508660460641434022020257614450354085808398293279060446966692082427506909617283562394303716193372887306176319841941848888379308208426966697446699225783646634631703732019477632822374479322570142967559738439193417309205283438893083349863592921249218168590490390313109776446516881569691499831380592661740653935515397472059631417493981532",
                    "name": "25134437486609445980011967476486104706321061312022352268621323694861467756181853100693555519614894168921947814126694858839278103549577703105305116890325322098078409416441750313062396467567140699008203113519528887729951138845002409659317083029073793314514377377412805387401717457417895322600145580639449003584446356048213839274172751441145076183734269045919984853749007476629365146654240675320041155618450449041510280560040162429566008590065069477149918088087715269037925211599101597422023202484497946662159070023999719865939258557778022770035320019440597702090334486792710436579355608406897769514395306079855023848170",
                    "height": "59326960517737425423547279838932030505937927873589489863081026714907925093402287263487670945897247474465655528290016645774365383046524346223348261262488616342337864633104758662753452450299389775751012589698563659277683974188553993694220606310980581680471280640591973543996299789038056921309016983827578247477799948667666717056420270448516049047961099547588510086600581628091290215485826514170097211360599793229701811672966818089371089216189744274422526431130783428589346341196561742409198605034972210917502326180305735092988639850309253190875578501020679137562856724998821945605494355779034135306337094344532980411836"
                },
                "rctxt": "9641986614889199796257508700106896585587271615330980339636468819377346498767697681332046156705231986464570206666984343024200482683981302064613556104594051003956610353281701880542337665385482309134369756144345334575765116656633321636736946947493150642615481313285221467998414924865943067790561494301461899025374692884841352282256044388512875752628313052128404892424405230961678931620525106856624692942373538946467902799339061714326383378018581568876147181355325663707572429090278505823900491548970098691127791086305310899642155499128171811034581730190877600697624903963241473287185133286356124371104261592694271730029",
                "z": "77594127026421654059198621152153180600664927707984020918609426112642522289621323453889995053400171879296098965678384769043918218957929606187082395048777546641833348694470081024386996548890150355901703252426977094536933434556202865213941384425538749866521536494046548509344678288447175898173634381514948562261015286492185924659638474376885655055568341574638453213864956407243206035973349529545863886325462867413885904072942842465859476940638839087894582648849969332663627779378998245133055807038199937421971988505911494931665143822588532097754480882750243126847177560978100527491344463525107644125030963904001009159559"
            },
            "revocation": None
        }
    }


@pytest.fixture(scope="module")
def credential_def_json(credential_def):
    return json.dumps(credential_def)


@pytest.fixture(scope="module")
async def prepopulated_wallet(wallet_handle, gvt_schema_json, xyz_schema_json, gvt_cred_values_json,
                              gvt_2_cred_values_json, xyz_cred_values_json, issuer_did, issuer_did_2, master_secret_id,
                              prover_did, tag, default_cred_def_config, id_credential_1, id_credential_2,
                              id_credential_3):
    # Create GVT credential by Issuer1
    (issuer1_gvt_cred_deg_id, issuer1_gvt_credential_def_json) = \
        await anoncreds.issuer_create_and_store_credential_def(wallet_handle, issuer_did, gvt_schema_json, tag,
                                                               None, default_cred_def_config)

    # Create XYZ credential by Issuer1
    (issuer1_xyz_cred_deg_id, issuer1_xyz_credential_def_json) = \
        await anoncreds.issuer_create_and_store_credential_def(wallet_handle, issuer_did, xyz_schema_json, tag,
                                                               None, default_cred_def_config)

    # Create GVT credential by Issuer2
    (issuer2_gvt_cred_def_id, issuer2_gvt_credential_def_json) = \
        await anoncreds.issuer_create_and_store_credential_def(wallet_handle, issuer_did_2, gvt_schema_json, tag,
                                                               None, default_cred_def_config)

    issuer_1_gvt_credential_offer_json = \
        await anoncreds.issuer_create_credential_offer(wallet_handle, issuer1_gvt_cred_deg_id)
    issuer_1_xyz_credential_offer_json = \
        await anoncreds.issuer_create_credential_offer(wallet_handle, issuer1_xyz_cred_deg_id)
    issuer_2_gvt_credential_offer_json = \
        await anoncreds.issuer_create_credential_offer(wallet_handle, issuer2_gvt_cred_def_id)

    await anoncreds.prover_create_master_secret(wallet_handle, master_secret_id)

    (issuer_1_gvt_cred_req, issuer_1_gvt_cred_req_metadata) = \
        await anoncreds.prover_create_credential_req(wallet_handle, prover_did, issuer_1_gvt_credential_offer_json,
                                                     issuer1_gvt_credential_def_json, master_secret_id)

    (issuer_1_gvt_cred, _, _) = \
        await anoncreds.issuer_create_credential(wallet_handle, issuer_1_gvt_credential_offer_json,
                                                 issuer_1_gvt_cred_req, gvt_cred_values_json, None, None)

    await anoncreds.prover_store_credential(wallet_handle, id_credential_1, issuer_1_gvt_cred_req,
                                            issuer_1_gvt_cred_req_metadata,
                                            issuer_1_gvt_cred, issuer1_gvt_credential_def_json, None, None)

    (issuer_1_xyz_cred_req, issuer_1_xyz_cred_req_metadata) = \
        await anoncreds.prover_create_credential_req(wallet_handle, prover_did, issuer_1_xyz_credential_offer_json,
                                                     issuer1_xyz_credential_def_json, master_secret_id)

    (issuer_1_xyz_cred, _, _) = \
        await anoncreds.issuer_create_credential(wallet_handle, issuer_1_xyz_credential_offer_json,
                                                 issuer_1_xyz_cred_req, xyz_cred_values_json, None, None)

    await anoncreds.prover_store_credential(wallet_handle, id_credential_2, issuer_1_xyz_cred_req,
                                            issuer_1_xyz_cred_req_metadata, issuer_1_xyz_cred,
                                            issuer1_xyz_credential_def_json, None, None)

    (issuer_2_gvt_cred_req, issuer_2_gvt_cred_req_metadata) = \
        await anoncreds.prover_create_credential_req(wallet_handle, prover_did, issuer_2_gvt_credential_offer_json,
                                                     issuer2_gvt_credential_def_json, master_secret_id)

    (issuer_2_gvt_cred, _, _) = \
        await anoncreds.issuer_create_credential(wallet_handle, issuer_2_gvt_credential_offer_json,
                                                 issuer_2_gvt_cred_req, gvt_2_cred_values_json, None, None)

    await anoncreds.prover_store_credential(wallet_handle, id_credential_3, issuer_2_gvt_cred_req,
                                            issuer_2_gvt_cred_req_metadata,
                                            issuer_2_gvt_cred, issuer2_gvt_credential_def_json, None, None)

    return issuer1_gvt_credential_def_json, issuer_1_gvt_credential_offer_json, issuer_1_gvt_cred_req, \
           issuer_1_gvt_cred_req_metadata, issuer_1_gvt_cred,
