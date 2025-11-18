# Progress Tracking Design Document

## Overview
This document details the architectural design for implementing time calculation and progress tracking in the PDF OCR script.

## Architecture

### Current State
The existing system processes PDFs page by page without any progress feedback or time measurements. Users must wait for the entire process to complete without knowing the status.

### Proposed Architecture
```
PDF Input -> Page Extraction -> [Progress Tracking] -> Image Processing -> LMStudio API -> [Time Calculation] -> Markdown Output -> [Performance Summary]
```

### Components

#### 1. Progress Tracker
- Uses tqdm for visual progress bar
- Shows percentage complete, pages processed, and total pages
- Displays estimated time remaining (ETA)

#### 2. Time Calculator
- Measures overall processing time from start to finish
- Calculates individual page processing times
- Computes averages and performance metrics

#### 3. ETA Estimator
- Calculates based on average processing time per page
- Updates in real-time as processing continues
- Provides reasonable estimates even for variable processing times

#### 4. Performance Reporter
- Compiles statistics about the processing session
- Reports pages per second, total time, and efficiency metrics
- Provides feedback for optimization opportunities

## Data Flow

1. The system loads a PDF file and counts total pages
2. Initialize progress tracker with total page count
3. Record overall start time
4. For each page:
   - Record page start time
   - Process the page (image conversion, API call)
   - Record page end time
   - Update progress bar with time data
   - Calculate updated ETA
5. Calculate total processing time
6. Generate performance summary

## Implementation Details

- Use tqdm for progress visualization
- Add time.perf_counter() for accurate time measurement
- Implement ETA calculation based on average page processing time
- Format time values in human-readable format (HH:MM:SS)

## Error Handling

- Maintain progress tracking even if individual pages fail
- Handle API errors gracefully without breaking progress flow
- Provide meaningful error messages with time context