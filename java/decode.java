import java.io.*;
import java.util.*;


public class TestClass {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter wr = new PrintWriter(System.out);
        int T = Integer.parseInt(br.readLine().trim());
        for(int t_i=0; t_i<T; t_i++)
        {
            String s = br.readLine();

            String out_ = decode(s);
            System.out.println(out_);
         }

         wr.close();
         br.close();
    }
    static String decode(String s){
        int len = s.length();
        int mid,temp = 0, c = 1;
        if(len % 2 != 0){
            mid = len/2 + 1;
        } else{
            mid = len/2;
        }
        char ch[] = new char[len +1];
        
        if(len%2 != 0){
            ch[mid] = s.charAt(0);
            for(int i=1;i<len;i++){
                if(i%2 != 1){
                    ch[mid+c] = s.charAt(i);
                }else{
                    ch[mid-c] = s.charAt(i);
                }
                temp+=1;
                if(temp == 2){
                    c+=1;
                    temp = 0;
                }
            }
        }else{
            ch[mid] = s.charAt(0);
            for(int i=1;i<len;i++){
                if(i%2 != 0){
                    ch[mid+c] = s.charAt(i);
                }else{
                    ch[mid-c] = s.charAt(i);
                }
                temp += 1;
                if(temp == 2){
                    c += 1;
                    temp = 0;
                }
            }
        }
        String str = new String(ch);
        return str.trim();
        
    }
}