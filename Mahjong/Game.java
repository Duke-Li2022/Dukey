package gui;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Random;
import java.util.Scanner;

public class Game {
    static private int [] cards = new int[34];
    static private int [] p1 = new int[34];
    static private int [] p2 = new int[34];
    static private int [] p3 = new int[34];
    static private int [] p4 = new int[34];
    static private String[] cardname = { "1万", "2万", "3万", "4万", "5万", "6万", "7万", "8万", "9万",
            "1条", "2条", "3条", "4条", "5条", "6条", "7条", "8条", "9条",
            "1筒", "2筒", "3筒", "4筒", "5筒", "6筒", "7筒", "8筒", "9筒",
            "东风", "南风", "西风", "北风", "红中", "发财", "白板"};
    private static final HashMap<String, Integer> tileToIndex = new HashMap<>();


    public static int findIndex(String tileName) {
        return tileToIndex.getOrDefault(tileName, -1);
    }
    public static void main(String[] args) {
        startGame();
        boolean flag = true;
//        for (int i = 0; i < 34; i++) {
//            p1[i] = 0;
//        }
//        p1[0] = 3;
//        p1[1] = 3;
//        p1[2] = 3;
//        p1[3] = 3;
        int index = 1;
        Scanner scanner = new Scanner(System.in);
        while (flag){
            int[] temp = null;
            Random random = new Random();
            if(index == 1){
                int num = 0;
                while (num < 1){
                    int aim = random.nextInt(0,34);
                    if(drawCard(aim,p1)){
                        num++;
                    }
                }
                //p1[5] = 2;
                temp = p1;
            }
            else if(index == 2){
                int num = 0;
                while (num < 1){
                    int aim = random.nextInt(0,34);
                    if(drawCard(aim,p2)){
                        num++;
                    }
                }
                temp = p2;
            }
            else if(index == 3){
                int num = 0;
                while (num < 1){
                    int aim = random.nextInt(0,34);
                    if(drawCard(aim,p3)){
                        num++;
                    }
                }
                temp = p3;
            }
            else if(index == 4){
                int num = 0;
                while (num < 1){
                    int aim = random.nextInt(0,34);
                    if(drawCard(aim,p4)){
                        num++;
                    }
                }
                temp = p4;
            }
            System.out.println("现在是玩家"+index+"的回合，选择弃牌或者胡：");
            boolean smallfalg = true;
            printHand(temp);
            while (smallfalg){
                String s = scanner.nextLine();
                if(s.equals("胡")){
                    if(win(temp)){
                        flag = false;
                        smallfalg = false;
                        System.out.println("玩家"+index+"胜利");
                    }else {
                        System.out.println("继续输入：");
                    }
                }else {
                    if(discard(s,temp)){
                        smallfalg = false;
                        System.out.println("弃牌后手牌：");
                        printHand(temp);
                    }else {
                        System.out.println("继续输入：");
                    }
                }
            }
            printHub();
            index++;

            if(index == 5){
                index = 1;
            }
        }
    }
    public static boolean discard(String tilename, int[] player){
        int index = findIndex(tilename);
        if(index == -1 || player[index] == 0){
            System.out.println("无法弃牌");
            return false;
        }
        player[index]--;
        return true;
    }
    public static boolean win(int[] player){
        int[] temp = Arrays.copyOf(player,player.length);
        int index = 0;
        for (int i = 0; i < player.length; i++) {
            if(temp[i] >= 3){
                temp[i] -= 3;
                index++;
            }
        }
        for (int i = 0; i <= 24; i++) {
            if(i <= 6){
                if(temp[i] >= 1 && temp[i+1] >= 1 && temp[i+2] >= 1){
                    temp[i]--;
                    temp[i+1]--;
                    temp[i+2]--;
                    index++;
                }
            }else if(i>8&&i<=15){
                if(temp[i] >= 1 && temp[i+1] >= 1 && temp[i+2] >= 1){
                    temp[i]--;
                    temp[i+1]--;
                    temp[i+2]--;
                    index++;
                }
            } else if (i>17&&i<=24) {
                if(temp[i] >= 1 && temp[i+1] >= 1 && temp[i+2] >= 1){
                    temp[i]--;
                    temp[i+1]--;
                    temp[i+2]--;
                    index++;
                }
            }
        }
        if(temp[27]>=1&&temp[28]>=1&&temp[29]>=1){
            temp[27]--;
            temp[28]--;
            temp[29]--;
            index++;
        }
        if(temp[27]>=1&&temp[28]>=1&&temp[30]>=1){
            temp[27]--;
            temp[28]--;
            temp[30]--;
            index++;
        }
        if(temp[27]>=1&&temp[29]>=1&&temp[30]>=1){
            temp[27]--;
            temp[29]--;
            temp[30]--;
            index++;
        }
        if(temp[31]>=1&&temp[32]>=1&&temp[33]>=1){
            temp[31]--;
            temp[32]--;
            temp[33]--;
            index++;
        }
        if(index == 4){
            for (int i = 0; i < temp.length; i++) {
                if(temp[i] == 2){
                    return true;
                }
            }
        }
        System.out.println("不能胡");
        return false;
    }
    public static void startGame(){
        for (int i = 0; i < cardname.length; i++) {
            tileToIndex.put(cardname[i], i);
        }
        for (int i = 0; i < 34; i++) {
            cards[i] = 4;
        }
        Random random = new Random();
        int num = 0;
        while (num < 13){
            int index = random.nextInt(0,34);
            if(drawCard(index,p1)){
                num++;
            }
        }
        num = 0;
        while (num < 13){
            int index = random.nextInt(0,34);
            if(drawCard(index,p2)){
                num++;
            }
        }
        num = 0;
        while (num < 13){
            int index = random.nextInt(0,34);
            if(drawCard(index,p3)){
                num++;
            }
        }
        num = 0;
        while (num < 13){
            int index = random.nextInt(0,34);
            if(drawCard(index,p4)){
                num++;
            }
        }
        printHub();
        System.out.println("玩家1手牌：");
        printHand(p1);
        System.out.println("玩家2手牌：");
        printHand(p2);
        System.out.println("玩家3手牌：");
        printHand(p3);
        System.out.println("玩家4手牌：");
        printHand(p4);

    }
    public static boolean drawCard(int index, int[] player){
        if(cards[index] != 0){
            cards[index]--;
            player[index]++;
            return true;
        }return false;
    }
    public static void printHand(int[] player){
        for (int i = 0; i < 34; i++) {
            if(player[i] != 0){
                for (int j = 0; j < player[i]; j++) {
                    System.out.print(cardname[i]+" ");
                }
            }
        }
        System.out.println();
    }
    public static void printHub(){
        System.out.println("牌库：");
        for (int i = 0; i < 34; i++) {
            System.out.print(cardname[i]+":" + cards[i]+" ");
            if(i == 8 || i == 17 || i == 26){
                System.out.println();
            }
        }
        System.out.println();
    }
}
