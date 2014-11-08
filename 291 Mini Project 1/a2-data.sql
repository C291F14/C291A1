--
-- Assignment 2 Database 
-- Cody Ingram
--

-- Populate Medical_lab table

insert into medical_lab values ('Edmonton West','780 Edmonton Rd.', '7809102014');
insert into medical_lab values ('CMPUT Lab', '10110 CMPUT Ridge', '8881010110');
insert into medical_lab values ('Calgary Lab', '587 Calgary Blvd.', '5874446666');
insert into medical_lab values ('Vancouver Lab', '604 Vancouver Way', '6042984567');
insert into medical_lab values ('UofA Lab',  '291 Ualberta Estates', '2912911000');


-- Populate patient table

insert into patient values (123456, 'Adam', '291 Kensington Way', TO_DATE('19221010', 'YYYYMMDD'), '5879874576');
insert into patient values (456789, 'Bob', '291 Coogee Blvd.', TO_DATE('19451212', 'YYYYMMDD'), '6045847396');
insert into patient values (789123, 'Chuck', '291 Edmonton Ridge', TO_DATE('19690101', 'YYYYMMDD'), '7803903827');
insert into patient values (121322, 'David', '291 Kensington Rd.', TO_DATE('19861015', 'YYYYMMDD'), '5879473957');
insert into patient values (853065, 'George', '291 Maroubra', TO_DATE('20141016', 'YYYYMMDD'), '5848376594');
insert into patient values (936184, 'Graham', '291 Maroubra', TO_DATE('20010604', 'YYYYMMDD'), '8473485747');
insert into patient values (493756, 'Greg', '291 Coogee Way', TO_DATE('19990918', 'YYYYMMDD'), '6048574747');
insert into patient values (104638, 'Ian', '291 Edmonton Rd.', TO_DATE('19881112', 'YYYYMMDD'), '7804837287');
insert into patient values (285836, 'Jack', '291 Edmonton St.', TO_DATE('18670110', 'YYYYMMDD'), '1747396790');
insert into patient values (298476, 'James', '291 Edmonton Ave', TO_DATE('19790615', 'YYYYMMDD'), '7807503759');
insert into patient values (947394, 'Jane', '291 Edmonton Blvd.', TO_DATE('19470506', 'YYYYMMDD'), '9473949483');
insert into patient values (293740, 'Jenny', '291 La Perouse', TO_DATE('19480404', 'YYYYMMDD'), '9003927848');
insert into patient values (380275, 'Jill', '291 Malabar', TO_DATE('19780503', 'YYYYMMDD'), '4739568384');
insert into patient values (184373, 'Jim', '291 Maroubra', TO_DATE('20120101', 'YYYYMMDD'), '9493395737');
insert into patient values (324532, 'Joe', '291 Randwick Ave.', TO_DATE('20000101', 'YYYYMMDD'), '3038384737');
insert into patient values (394857, 'John', '291 Kensington Blvd.', TO_DATE('19890920', 'YYYYMMDD'), '5879738458');
insert into patient values (908344, 'Keith', '291 Redfern Rd.', TO_DATE('19570411', 'YYYYMMDD'), '4947087734');
insert into patient values (485646, 'Steve', '291 Coogee Palace', TO_DATE('19570412', 'YYYYMMDD'), '6049485585');
insert into patient values (678754, 'Tony', '291 Coogee Pass', TO_DATE('19700510', 'YYYYMMDD'), '6044089687');
insert into patient values (876543, 'Victor', '291 Randwick Rd.', TO_DATE('19380703', 'YYYYMMDD'), '2394872934');
insert into patient values (456776, 'Wayne', '291 Kingsford St.', TO_DATE('19970302', 'YYYYMMDD'), '2342342342');
insert into patient values (136202, 'Cody', '291 Edmonton Way', TO_DATE('19941017', 'YYYYMMDD'), '7809029898');

-- Populate doctor table

insert into doctor values (1256, '291 Whoville Blvd.', '3957294827', '9119473927', 123456);
insert into doctor values (1394, '291 Fort Knox', '9374957382', '9118473639', 853065);
insert into doctor values (1945, '291 Sesame Ave', '3950281759', '9118568395', 380275);
insert into doctor values (1746, '291 Yellow Brick Rd.', '9012958773', '9112094838', 136202);
insert into doctor values (1374, '291 Lampwrights St.', '1047583743', '9118493745', 947394);

-- Populate test_type table

insert into test_type values (10, 'CT scan', 'must have a Zerox perscription', 'Scan using the scanners');
insert into test_type values (20, 'bone marrow check', 'Must have bone marrow', 'Check the marrow inside the bones');
insert into test_type values (30, 'X ray', 'must have bones', 'Scan the person with x rays');
insert into test_type values (40, 'blood test', 'must have blood', 'Take blood and put into container');
insert into test_type values (50, 'brain transplant', 'must have heart. Brain not required', 'Remove old brain if neccessary. Put in new one');

-- Populate can_conduct table

insert into can_conduct values ('Edmonton West', 10);
insert into can_conduct values ('Edmonton West', 30);
insert into can_conduct values ('CMPUT Lab', 20);
insert into can_conduct values ('CMPUT Lab', 30);
insert into can_conduct values ('CMPUT Lab', 50);
insert into can_conduct values ('Calgary Lab', 40);
insert into can_conduct values ('Vancouver Lab', 40);
insert into can_conduct values ('Vancouver Lab', 10);
insert into can_conduct values ('UofA Lab', 10);
insert into can_conduct values ('UofA Lab', 30);
insert into can_conduct values ('UofA Lab', 50);

-- Populate not_allowed table

insert into not_allowed values (136202, 50);
insert into not_allowed values (104638, 20);
insert into not_allowed values (104638, 40);
insert into not_allowed values (908344, 20);
insert into not_allowed values (876543, 40);
insert into not_allowed values (293740, 10);
insert into not_allowed values (293740, 30);

-- Populate test_record table

insert into test_record values(123, 20, 123456, 1394, 'CMPUT Lab', 'normal', TO_DATE('20100503', 'YYYYMMDD'), TO_DATE('20100704', 'YYYYMMDD'));
insert into test_record values(122, 20, 123456, 1394, 'CMPUT Lab', 'normal', TO_DATE('20120501', 'YYYYMMDD'), TO_DATE('20120909', 'YYYYMMDD'));
insert into test_record values(133, 40, 123456, 1256, 'Vancouver Lab', 'result: E=MC^2', TO_DATE('20120403', 'YYYYMMDD'), TO_DATE('20120609', 'YYYYMMDD'));
insert into test_record values(111, 10, 456789, 1374,'Vancouver Lab', 'result: fully scanned', TO_DATE('20130106', 'YYYYMMDD'), TO_DATE('20130505', 'YYYYMMDD'));
insert into test_record values(132, 10, 789123, 1945,'UofA Lab', 'result: pass', TO_DATE('20140105', 'YYYYMMDD'), TO_DATE('20140107', 'YYYYMMDD'));
insert into test_record values(100, 20, 121322, 1945,'CMPUT Lab', 'normal', TO_DATE('20100804', 'YYYYMMDD'), TO_DATE('20100902', 'YYYYMMDD'));
insert into test_record values(101, 30, 853065, 1394, 'Edmonton West', 'normal', TO_DATE('20130407', 'YYYYMMDD'), TO_DATE('20140603', 'YYYYMMDD'));
insert into test_record values(102, 40, 936184, 1374,'Vancouver Lab', 'result: good test', TO_DATE('20120308', 'YYYYMMDD'), TO_DATE('20120604', 'YYYYMMDD'));
insert into test_record values(103, 30, 104638, 1374,'UofA Lab', 'normal', TO_DATE('20100505', 'YYYYMMDD'), TO_DATE('20110307', 'YYYYMMDD'));
insert into test_record values(164, 50, 104638, 1945,'CMPUT Lab', 'result: this was an excellent test', TO_DATE('20130703', 'YYYYMMDD'), TO_DATE('20130402', 'YYYYMMDD'));
insert into test_record values(163, 50, 285836, 1374,'UofA Lab', 'result: awesome', TO_DATE('20130408', 'YYYYMMDD'), TO_DATE('20130708', 'YYYYMMDD'));
insert into test_record values(136, 50, 947394, 1374, 'UofA Lab', 'result: brain succesfully planted', TO_DATE('20110209', 'YYYYMMDD'), TO_DATE('20110204', 'YYYYMMDD'));
insert into test_record values(147, 10, 324532, 1374,'Vancouver Lab', 'result: scan successful', TO_DATE('20130205', 'YYYYMMDD'), TO_DATE('20110903', 'YYYYMMDD'));
insert into test_record values(138, 40, 136202, 1746, 'Calgary Lab', 'result: no blood', TO_DATE('20110903', 'YYYYMMDD'), TO_DATE('20110906', 'YYYYMMDD'));
insert into test_record values(193, 10, 678754, 1256,'Edmonton West', 'normal', TO_DATE('20131107', 'YYYYMMDD'), TO_DATE('20120709', 'YYYYMMDD'));
insert into test_record values(137, 30, 908344, 1746,'Edmonton West', 'result: bones broken', TO_DATE('20140704', 'YYYYMMDD'), TO_DATE('20140306', 'YYYYMMDD'));
insert into test_record values(128, 10, 678754, 1256,'Calgary Lab', 'result: blood is O-', TO_DATE('20131108', 'YYYYMMDD'), TO_DATE('20130402', 'YYYYMMDD'));
insert into test_record values(195, 10, 678754, 1256,'Vancouver Lab', 'result: blood is A+', TO_DATE('20131108', 'YYYYMMDD'), TO_DATE('20120601', 'YYYYMMDD'));
insert into test_record values(148, 20, 293740, 1746,'CMPUT Lab', 'result: has bone marrow', TO_DATE('20120308', 'YYYYMMDD'), TO_DATE('20120601', 'YYYYMMDD'));
insert into test_record values(199, 10, 456789, 1374,'Vancouver Lab', 'normal', TO_DATE('20130106', 'YYYYMMDD'), TO_DATE('20130505', 'YYYYMMDD'));
insert into test_record values(167, 10, 456789, 1374,'Vancouver Lab', 'result: fully scanned', TO_DATE('20130109', 'YYYYMMDD'), TO_DATE('20130406', 'YYYYMMDD'));
insert into test_record values(173, 10, 456789, 1374,'Vancouver Lab', 'result: fully scanned', TO_DATE('20130107', 'YYYYMMDD'), TO_DATE('20130307', 'YYYYMMDD'));
insert into test_record values(183, 10, 456789, 1746,'Vancouver Lab', 'result: fully scanned', TO_DATE('20131107', 'YYYYMMDD'), TO_DATE('20131107', 'YYYYMMDD'));
insert into test_record values(175, 40, 456789, 1746,'Vancouver Lab', 'result: fully scanned', TO_DATE('20131107', 'YYYYMMDD'), TO_DATE('20131107', 'YYYYMMDD'));
insert into test_record values(178, 10, 456789, 1746,'Vancouver Lab', 'result: fully scanned', TO_DATE('20131107', 'YYYYMMDD'), TO_DATE('20131107', 'YYYYMMDD'));
