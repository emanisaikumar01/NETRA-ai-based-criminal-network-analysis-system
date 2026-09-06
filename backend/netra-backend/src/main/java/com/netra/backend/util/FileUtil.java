package com.netra.backend.util;

import java.nio.file.Path;

public final class FileUtil {

    private FileUtil() {
        // Utility class
    }

    /**
     * Extracts the file extension.
     *
     * Example:
     * document.pdf -> pdf
     * image.JPG -> jpg
     */
    public static String extension(String fileName) {

        if (fileName == null || fileName.isBlank()) {
            return "";
        }

        int lastDot = fileName.lastIndexOf('.');

        if (lastDot == -1 || lastDot == fileName.length() - 1) {
            return "";
        }

        return fileName
                .substring(lastDot + 1)
                .toLowerCase();
    }

    /**
     * Removes any directory path from the filename.
     *
     * Example:
     * C:\Users\User\Documents\report.pdf
     * becomes:
     * report.pdf
     */
    public static String safeFileName(String fileName) {

        if (fileName == null || fileName.isBlank()) {
            return "";
        }

        return Path.of(fileName)
                .getFileName()
                .toString();
    }
}