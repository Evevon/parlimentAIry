
/* questions table contains all questions that need to be answered.
 * The code below makes the questions table. The name for the database
 * is parlimentairy. Once this database is generated, put the code below
 * into the SQL tab.
 */
create table questions(
    id int(255) not null PRIMARY KEY AUTO_INCREMENT,
    status varchar(30) not null,
    name varchar(30) not null,
    description varchar(200) not null
);

insert into questions (status, name, description) VALUES ('todo','gevolgen van brexit', 'De Brexit heeft ongetwijfeld gevolgen op de afspraken tussen Engeland en Nederland. Kan de minister deze in kaart brengen?');
insert into questions (status, name, description) VALUES ('todo','budget voor aanleg weg', 'Er wordt een nieuwe weg aangelegd tussen Utrecht en Amsterdam, is de minister het eens met het huidige budget dat hiervoor vaststaat?');
insert into questions (status, name, description) VALUES ('todo','milieu en nieuwbouw', 'Wat denkt de minister van de nieuwe maatregelen om nieuwbouw milieuvriendelijk te maken?');
insert into questions (status, name, description) VALUES ('todo','vragen over de stint', 'De stint maakt het verkeer onveilig, maar kinderen moeten wel vervoerd kunnen worden. Wat is het beste alternatief?');
insert into questions (status, name, description) VALUES ('todo','vragen over scootmobiels', 'De laatste tijd zegt men dat scootmobiels niet veilig voor het verkeer. Wat zijn de cijfers m.b.t. de ongelukken met scootmobiels?');
insert into questions (status, name, description) VALUES ('inprogress','uitbreiding schiphol', 'Schiphol wil uitbreiden, maar de omwoners willen dit niet vanwege geluidsoverlast. Is er data beschikbaar over geluidsmetingen in deze wijken?');

