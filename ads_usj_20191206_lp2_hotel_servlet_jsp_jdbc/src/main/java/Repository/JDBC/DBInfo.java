package Repository.JDBC;

class DBInfo {

    private static String driver = "com.mysql.cj.jdbc.Driver";
    private static String url = "jdbc:mysql://localhost:3306/hotel?useTimezone=true&serverTimezone=UTC&useSSL=true";
    private static String user = "root";
    private static String pass = "entrar";

    public static String getDriver() {
        return driver;
    }

    public static String getUrl() {
        return url;
    }

    public static String getUser() {
        return user;
    }

    public static String getPass() {
        return pass;
    }
}
