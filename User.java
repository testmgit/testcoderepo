public class User {
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

    // Getter 和 Setter 方法
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        if (age >= 0) {
            this.age = age;
        }
    }

    public boolean isActive() {
        return isActive;
    }

    public void setActive(boolean active) {
        isActive = active;
    }

    // 业务方法
    public void displayUserInfo() {
        System.out.println("Username: " + username);
        System.out.println("Email: " + email);
        System.out.println("Age: " + age);
        System.out.println("Active: " + isActive);
    }

    // 验证邮箱格式
    public boolean isValidEmail() {
        return email != null && email.contains("@") && email.contains(".");
    }
}