public static void main(String[] args)
  {
    String s = "aabbaabbcdc";
    StringBuilder sb = new StringBuilder();
    boolean[] seen = new boolean[256];
    for(int i = 0 ; i < s.length(); i++){
      if(!seen[(int)s.charAt(i)]){
      	seen[(int)s.charAt(i)] = true;
        sb.append(s.charAt(i));
      }
    }
    System.out.println(sb.toString());
  }
