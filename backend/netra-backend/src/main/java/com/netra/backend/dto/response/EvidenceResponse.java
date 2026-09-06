package com.netra.backend.dto.response;

public record EvidenceResponse(

        String id,

        String caseId,

        String fileName,

        String fileType,

        long fileSize,

        String status,

        String message

) {
}