import java.io.RandomAccessFile;
import java.nio.channels.FileChannel;
import java.nio.channels.FileLock;

public class FileLockExample {

    public static void main(String[] args) {

        try {
            // Open or create the file
            RandomAccessFile file =
                    new RandomAccessFile("data.txt", "rw");

            // Get the FileChannel
            FileChannel channel = file.getChannel();

            // Lock the file
            FileLock lock = channel.lock();

            System.out.println("File is locked!");

            // Write something to the file
            file.writeBytes("This file is currently locked.\n");

            // Keep the file locked for 5 seconds
            Thread.sleep(5000);

            // Release the lock
            lock.release();

            System.out.println("File lock released!");

            // Close channel and file
            channel.close();
            file.close();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}