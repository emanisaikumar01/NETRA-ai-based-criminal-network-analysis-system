package com.netra.backend.controller;

import com.netra.backend.dto.response.EvidenceResponse;
import com.netra.backend.service.EvidenceService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/evidence")
public class EvidenceController {

    private final EvidenceService evidenceService;

    public EvidenceController(
            EvidenceService evidenceService
    ) {
        this.evidenceService = evidenceService;
    }

    @GetMapping("/{id}")
    public ResponseEntity<EvidenceResponse> getEvidenceById(
            @PathVariable String id
    ) {

        return ResponseEntity.ok(
                evidenceService.getEvidenceById(id)
        );
    }

    @GetMapping("/case/{caseId}")
    public ResponseEntity<List<EvidenceResponse>> getEvidenceByCaseId(
            @PathVariable String caseId
    ) {

        return ResponseEntity.ok(
                evidenceService.getEvidenceByCaseId(caseId)
        );
    }
}