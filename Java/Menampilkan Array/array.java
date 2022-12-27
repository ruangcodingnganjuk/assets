import java.util.Arrays;

public class Main {
   public static void main(String[] args) {
      String[][] array = {
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
      int n = 10; // Jumlah data saat ini dalam array

      // Menampilkan isi array yang UKM-nya Olahraga
      for (int i = 0; i < n; i++) {
         if (array[i][2].equals("Olahraga")) {
            System.out.println("NIM: " + array[i][0] + System.lineSeparator() + "NAMA: " + array[i][1] + System.lineSeparator() + "UKM: " + array[i][2]);
            System.out.println("----------------------------------------------------------------------------------------------------------------------");
         }
      }
   }
}
