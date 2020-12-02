package lpi.projetofinal.dao.jdbc;

class DBInfo {
    
    private static String driver = "com.mysql.jdbc.Driver";
//    private static String driver = "com.mysql.cj.jdbc.Driver";
    private static String url = "jdbc:mysql://172.18.0.2:3306/radio_ensino?useTimezone=true&serverTimezone=UTC";
    private static String user = "root";
    private static String pass = "123456";
    // private static String url = "jdbc:mysql://192.185.173.161:3306/radio_ensino"; //?useTimezone=true&serverTimezone=UTC"
    // private static String user = "radio_admin";
    // private static String pass = "etec2017";

    
    public static String getDriver(){
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
