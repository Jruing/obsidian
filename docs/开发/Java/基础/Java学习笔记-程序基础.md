
## 程序结构
```java
/**
 * 文件名称：Hello.java,文件名需要和类名称保持一致
 * 可以用来自动创建文档的注释
 */

// 关键字 class
// 类名 Hello
public class Hello {
    // 关键字 static，代表静态方法，java入口程序必须为静态方法
    // 返回值类型 void，代表无返回值
    // 方法名 main
    public static void main(String[] args) {
        // 向屏幕输出文本:
        System.out.println("Hello, world!");
    }
}
```
## 变量
## 定义变量
```java
// 格式为：类型 变量名 = 值
// 定义一个类型为int，变量名为x，值为1的变量
int x = 1
```
### 基本数据类型
    整数类型：byte，short，int，long
    浮点数类型：float，double
    字符类型：char
    布尔类型：boolean
#### 整型
    byte：-128 ~ 127
    short: -32768 ~ 32767
    int: -2147483648 ~ 2147483647
    long: -9223372036854775808 ~ 9223372036854775807
```java
public class Main {
    public static void main(String[] args) {
        int i = 2147483647;
        int i2 = -2147483648;
        int i3 = 2_000_000_000; // 加下划线更容易识别
        int i4 = 0xff0000; // 十六进制表示的16711680
        int i5 = 0b1000000000; // 二进制表示的512

        long n1 = 9000000000000000000L; // long型的结尾需要加L
        long n2 = 900; // 没有加L，此处900为int，但int类型可以赋值给long
        int i6 = 900L; // 错误：不能把long型赋值给int
    }
}
```
特别注意：同一个数的不同进制的表示是完全相同的，例如15=0xf＝0b1111。
#### 浮点型
```java
// 对于float类型，需要加上f后缀。
float f1 = 3.14f;
float f2 = 3.14e38f; // 科学计数法表示的3.14x10^38
float f3 = 1.0; // 错误：不带f结尾的是double类型，不能赋值给float

double d = 1.79e308;
double d2 = -1.79e308;
double d3 = 4.9e-324; // 科学计数法表示的4.9x10^-324
```
#### 布尔类型
```java
boolean b1 = true;
boolean b2 = false;
boolean isGreater = 5 > 3; // 计算结果为true
int age = 12;
boolean isAdult = age >= 18; // 计算结果为false
```
#### 字符类型
```java
// 字符类型
public class Main {
    public static void main(String[] args) {
        char a = 'A';
        char zh = '中';
        System.out.println(a);
        System.out.println(zh);
    }
}
```
#### 引用类型
```java
String s = "hello";
```
#### 常量
```java
final double PI = 3.14; // PI是一个常量
double r = 5.0;
double area = PI * r * r;
PI = 300; // compile error!
```
#### var关键字
`var` 声明的变量必须进行初始化
```java
StringBuilder sb = new StringBuilder();
// 等同于上面
var sb = new StringBuilder();
```
## 整数运算
### 移位运算
### 位运算
### 自增/自减
