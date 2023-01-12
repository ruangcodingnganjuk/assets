import java.util.Arrays;

public class Main {
    public static int NIM = 0;
    public static int NAMA = 1;
    public static int UKM = 2;

    static String[][] array = {
            {"1234567890", "Adi", "Kepanitiaan"},
            {"0987654321", "Budi", "Olahraga"},
            {"1231231230", "Citra", "Musik"},
            {"9876543210", "Dedi", "Kepanitiaan"},
            {"1111111111", "Eka", "Olahraga"},
            {"2222222222", "Fajar", "Musik"},
            {"3333333333", "Galih", "Kepanitiaan"},
            {"4444444444", "Hasan", "Olahraga"},
            {"5555555555", "Irma", "Musik"},
            {"6666666666", "Jaka", "Kepanitiaan"}
    };
    static int n = 10; // Jumlah data saat ini dalam array

    public static void main(String[] args) {
        printData(NIM, "1234567890");
        printData(NAMA, "Adi");
        printData(UKM, "Olahraga");
    }

    public static void printData(int kategori, String kunci) {
        boolean status = false;
        // Menampilkan isi array yang sesuai dengan kategori dan kunci yang diberikan
        for (int i = 0; i < n; i++) {
            if (kategori == NIM && array[i][kategori].equals(kunci)) {
                status = true;
                System.out.println("STATUS: " + status + "\nNIM: " + array[i][0] + System.lineSeparator() + "NAMA: " + array[i][1] + System.lineSeparator() + "UKM: " + array[i][2] + System.lineSeparator());
            } else if (kategori == NAMA && array[i][kategori].equalsIgnoreCase(kunci)) {
                status = true;
                System.out.println("STATUS: " + status + "\nNIM: " + array[i][0] + System.lineSeparator() + "NAMA: " + array[i][1] + System.lineSeparator() + "UKM: " + array[i][2] + System.lineSeparator());
                
            } else if (kategori == UKM && array[i][kategori].equalsIgnoreCase(kunci)) {
                status = true;
                System.out.println("STATUS: " + status + "\nNIM: " + array  [i][0] + System.lineSeparator() + "NAMA: " + array[i][1] + System.lineSeparator() + "UKM: " + array[i][2] + System.lineSeparator());
                
            }
        }
        if (!status) {
            System.out.println("Data tidak ditemukan");
        }
    }
}
