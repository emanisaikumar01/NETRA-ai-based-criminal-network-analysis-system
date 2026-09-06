package com.netra.backend.service.impl;

import com.netra.backend.dto.request.UploadRequest;
import com.netra.backend.dto.response.EvidenceResponse;
import com.netra.backend.exception.BadRequestException;
import com.netra.backend.service.UploadService;
import com.netra.backend.util.FileUtil;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.util.Set;
import java.util.UUID;

@Service
public class UploadServiceImpl implements UploadService {

    private static final long MAX_FILE_SIZE =
            20 * 1024 * 1024; // 20 MB

    private static final Set<String> ALLOWED_EXTENSIONS =
            Set.of(
                    "pdf",
                    "txt",
                    "csv",
                    "jpg",
                    "jpeg",
                    "png",
                    "doc",
                    "docx"
            );

    @Override
    public EvidenceResponse uploadEvidence(
            UploadRequest request,
            MultipartFile file
    ) {

        validateFile(file);

        String fileName =
                FileUtil.safeFileName(file.getOriginalFilename());

        String extension =
                FileUtil.extension(fileName);

        String evidenceId =
                UUID.randomUUID().toString();

        return new EvidenceResponse(
                evidenceId,
                request.caseId(),
                fileName,
                extension,
                file.getSize(),
                "UPLOADED",
                "Evidence uploaded successfully"
        );
    }

    private void validateFile(MultipartFile file) {

        if (file == null || file.isEmpty()) {
            throw new BadRequestException(
                    "File is required"
            );
        }

        if (file.getSize() > MAX_FILE_SIZE) {
            throw new BadRequestException(
                    "File size must not exceed 20 MB"
            );
        }

        String fileName =
                FileUtil.safeFileName(file.getOriginalFilename());

        String extension =
                FileUtil.extension(fileName);

        if (!ALLOWED_EXTENSIONS.contains(extension)) {
            throw new BadRequestException(
                    "Unsupported file type: " + extension
            );
        }
    }
}