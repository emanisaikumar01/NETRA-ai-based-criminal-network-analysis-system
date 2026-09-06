package com.netra.backend.controller;

import com.netra.backend.dto.request.UploadRequest;
import com.netra.backend.dto.response.EvidenceResponse;
import com.netra.backend.service.UploadService;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
@RequestMapping("/api/uploads")
public class UploadController {

    private final UploadService uploadService;

    public UploadController(UploadService uploadService) {
        this.uploadService = uploadService;
    }

    @PostMapping(
            value = "/evidence",
            consumes = MediaType.MULTIPART_FORM_DATA_VALUE
    )
    public ResponseEntity<EvidenceResponse> uploadEvidence(
            @RequestParam("caseId") String caseId,

            @RequestParam(
                    value = "description",
                    required = false
            ) String description,

            @RequestPart("file") MultipartFile file
    ) {

        UploadRequest request =
                new UploadRequest(
                        caseId,
                        description
                );

        EvidenceResponse response =
                uploadService.uploadEvidence(
                        request,
                        file
                );

        return ResponseEntity
                .status(HttpStatus.CREATED)
                .body(response);
    }
}