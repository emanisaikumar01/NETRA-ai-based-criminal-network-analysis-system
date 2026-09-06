package com.netra.backend.controller;

import com.netra.backend.dto.request.CaseCreateRequest;
import com.netra.backend.dto.request.CaseUpdateRequest;
import com.netra.backend.dto.response.CaseResponse;
import com.netra.backend.service.CaseService;
import jakarta.validation.Valid;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/cases")
public class CaseController {

    private final CaseService caseService;

    public CaseController(CaseService caseService) {
        this.caseService = caseService;
    }

    @PostMapping
    public ResponseEntity<CaseResponse> createCase(
            @Valid @RequestBody CaseCreateRequest request
    ) {

        CaseResponse response =
                caseService.createCase(request);

        return ResponseEntity
                .status(HttpStatus.CREATED)
                .body(response);
    }

    @GetMapping
    public ResponseEntity<List<CaseResponse>> getAllCases() {

        return ResponseEntity.ok(
                caseService.getAllCases()
        );
    }

    @GetMapping("/{id}")
    public ResponseEntity<CaseResponse> getCaseById(
            @PathVariable String id
    ) {

        return ResponseEntity.ok(
                caseService.getCaseById(id)
        );
    }

    @PutMapping("/{id}")
    public ResponseEntity<CaseResponse> updateCase(
            @PathVariable String id,
            @Valid @RequestBody CaseUpdateRequest request
    ) {

        return ResponseEntity.ok(
                caseService.updateCase(id, request)
        );
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteCase(
            @PathVariable String id
    ) {

        caseService.deleteCase(id);

        return ResponseEntity.noContent().build();
    }
}