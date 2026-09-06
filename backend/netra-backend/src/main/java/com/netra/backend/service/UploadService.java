package com.netra.backend.service;

import com.netra.backend.dto.request.UploadRequest;
import com.netra.backend.dto.response.EvidenceResponse;
import org.springframework.web.multipart.MultipartFile;

public interface UploadService {

    EvidenceResponse uploadEvidence(
            UploadRequest request,
            MultipartFile file
    );
}