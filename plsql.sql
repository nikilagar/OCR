I)
declare
input varchar(20):='&input';
reverse varchar(20);
i integer(10);
begin
input:=:input;
for i in reverse 1..length(input)
loop
reverse:=reverse||substr(input,i,1);
end loop;
dbms_output.put_line('Reverse : '||reverse);
if input=reverse then
dbms_output.put_line('The given string '||input||' is a palindrome');
else
dbms_output.put_line('The given string '||input||' is not a palindrome');
end if;
end;
L)
DECLARE 
   code TEAM.TEAMCODE%type; 
   name TEAM.TEAMNAME%type; 
   country TEAM.COUNTRY%type; 
   CURSOR resultt is 
      SELECT t.teamcode, t.teamname,t.country FROM TEAM t,DRIVER d where t.teamcode=d.teamcode and d.birthdate>"1980-07-01"; 
BEGIN 
   OPEN resultt; 
   LOOP 
   FETCH resultt into code, name, country; 
      EXIT WHEN resultt%notfound; 
      dbms_output.put_line(code || ' ' || name || ' ' || country); 
   END LOOP; 
   CLOSE resultt; 
END; 