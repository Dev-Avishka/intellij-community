// "Move condition to loop" "true"
class Main {
  public static void main(String[] args) {
    int i = 0;
    for(;;) {
      if<caret>(i >= 12) break;
      i++;
    }
  }
}