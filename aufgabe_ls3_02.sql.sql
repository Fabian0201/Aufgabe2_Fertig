DROP DATABASE IF EXISTS cpu_monitoring;                       # Evtl. vorhandene Datenbank löschen

CREATE DATABASE cpu_monitoring default character set utf8;    # Neue Beispieldatenbank anlegen

USE cpu_monitoring;                                           # Mit neuer Datenbank verbinden

CREATE TABLE werte (                                        # Neue Tabelle in Beispieldatenbank anlegen
	t1_ID	int(11) NOT NULL AUTO_INCREMENT,
    t1_zeit	DATETIME DEFAULT NOW(),
    t1_wert	DECIMAL(9,2),
    ram DECIMAL(9,2),
    PRIMARY KEY (t1_ID)
    );
