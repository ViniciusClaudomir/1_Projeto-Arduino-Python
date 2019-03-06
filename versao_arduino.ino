int led1 = 13; // 
int red = 2;
int amarelo = 3;
int verde =4;
int mot = 5;
void setup(){
  Serial.begin(9600); // Velocidade padrão do Uno
  pinMode(led1, OUTPUT);
  pinMode(red, OUTPUT);
  pinMode(amarelo, OUTPUT);
  pinMode(verde, OUTPUT);// Porta onde o led será inserido, configurado como saida
  pinMode(mot, OUTPUT);// porta onde o relé será inserido, configurado como saida

  digitalWrite(mot,HIGH);//para o relé  "desativado" deixamos a porta como HIGH, ligada.
}
// conforme a necessidade, pode ser inserido novas variaveis, como os exemplos abaixo, lembre de incluir na def cor, e no //radiobutton no smartphone
void loop(){
  char leitura = Serial.read(); // Variavel que receberá os valores enviados pelo programa em python
  if(leitura == '1'){
    digitalWrite(verde, HIGH); // A variavel 1 do radiobutton estar relacionada com a cor verde
  }
  if(leitura == '0'){
    digitalWrite(verde, LOW);//A variavel 0 que é passada na vers_PC, é reponsavel por apagar o led
  }
  if(leitura == '2'){
    digitalWrite(amarelo, HIGH); // Liga a porta 13 se o valor recebido for 1
  }
  if(leitura == '3'){
    digitalWrite(amarelo, LOW);}
    
  if(leitura == '5'){
    digitalWrite(red, HIGH); // 
   }
  if(leitura == '6'){
    digitalWrite(red, LOW); // 
  }
  
  if(leitura == '7'){
    digitalWrite(led1, HIGH); // 
  }
  if(leitura == '8'){
    digitalWrite(led1, LOW);
  }
  if(leitura == '9'){
    digitalWrite(mot, LOW); //variavel 9 responsavel pelo relé
    delay(600);//apos o tempo, o relé é desligado automaticamente
    digitalWrite(mot, HIGH);
  }
  
}
