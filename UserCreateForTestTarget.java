public class UserCreateForTestTarget {
    // 用户属性
    private String username;
    private String email;
    private int age;
    private boolean isActive;

    // 构造函数
    public User(String username, String email, int age) {
        this.username = username;
        this.email = email;
        this.age = age;
        this.isActive = true;
    }

    public run(){
        print("run fast")
    }

}