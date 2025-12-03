using System;

namespace TestNamespace
{
    /// <summary>
    /// 用户创建测试目标类
    /// 对应 Python 的 UserCreateForTestTarget 类
    /// </summary>
    public class UserCreateForTestTarget
    {
        // 属性（对应 Python 的实例变量）
        public string Name { get; set; }
        public int Age { get; set; }

        /// <summary>
        /// 构造函数（对应 Python 的 __init__ 方法）
        /// </summary>
        /// <param name="name">用户名</param>
        /// <param name="age">年龄</param>
        public UserCreateForTestTarget(string name, int age)
        {
            this.Name = name;
            this.Age = age;
        }

        /// <summary>
        /// 运行方法（对应 Python 的 run 方法）
        /// </summary>
        public void Run()
        {
            Console.WriteLine("runnnnnnnnnn");
        }
    }
}